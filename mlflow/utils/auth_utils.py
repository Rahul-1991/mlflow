import os
import jwt
import json
import inspect
import sqlite3
from functools import wraps
from dotenv import load_dotenv, find_dotenv
from mlflow.exceptions import MlflowException
from mlflow.store.tracking.dbmodels.models import SqlUser
from mlflow.utils.user_role_access import role_access_map
from mlflow.protos.databricks_pb2 import PERMISSION_DENIED


def _get_user_data(username, password):
    sqlite_conn = sqlite3.connect('mlflow.db')
    sqlite_conn.row_factory = sqlite3.Row
    cursor = sqlite_conn.cursor()
    query = 'select * from user where username = "%s" and password = "%s"' % (username, password)
    cursor.execute(query)
    result = cursor.fetchall()
    return dict(result[0]) if result else dict()


def verify_user_credentials_from_env_file(jwt_token_path):
    os.environ.pop('AUTH_TOKEN', None)
    load_dotenv(jwt_token_path)
    auth_token = os.getenv('AUTH_TOKEN')
    secret_key = '004f2af45d3a4e161a7dd2d17fdae47f'
    data = jwt.decode(auth_token, secret_key, algorithms=["HS256"])
    user_data = _get_user_data(data.get('username'), data.get('password'))
    if not user_data:
        raise Exception('invalid User')
    return user_data


def _user_has_access(user_role, user_action, resource):
    for role, access in user_role.items():
        for action, resource_list in access.items():
            if action == user_action and (not resource or resource in resource_list):
                return True
    return False


def _is_operation_allowed(user_role, func_name, func_params):
    actions = ['experiment', 'model']
    user_roles = list()
    if func_name.startswith('_'):
        return True
    for role, access_data in user_role.items():
        if role_access_map.get(role):
            user_roles.extend(role_access_map.get(role))
    for role in user_roles:
        if role in ['get']:
            for action in actions:
                if role in func_name:
                    return _user_has_access(user_role, action, func_params)
        else:
            if role in func_name:
                return True
    return False


def assign_resource_to_user(user_role, resource_id, func_name, class_obj):
    actions = ['experiment', 'model']
    for action in actions:
        if action in func_name:
            if not user_role.get('PC'):
                user_role.update({'PC': {action: [resource_id]}})
            else:
                accessible_resources = user_role.get('PC', {}).get(action)
                accessible_resources.append(resource_id)
                user_role.get('PC').update({action: accessible_resources})
        with class_obj.ManagedSessionMaker() as session:
            session.query(SqlUser).filter(SqlUser.id == resource_id).update({'role': json.dumps(user_role)})
            session.flush()


def authorise_method_calls(func):
    @wraps(func)
    def wrapper(self, *args, **kw):
        # try:
        #     user_role = json.loads(self.user_data.get('role'))
        # except Exception as e:
        #     user_role = dict()
        user_role = {'PV': {'experiment': ["exp2"]}}
        if func.__name__ in ('__init__', 'get_jwt_auth_token'):
            func(self, *args, **kw)
        else:
            args1, varargs1, keywords1, defaults1 = inspect.getargspec(func)
            experiment_param = None
            for index, param in enumerate(args1):
                if param == 'experiment_id' or param == 'experiment_name':
                    experiment_param = args[index - 1]
            if _is_operation_allowed(user_role, func.__name__, experiment_param):
                if 'create' in func.__name__:
                    resource_id = func(self, *args, **kw)
                    assign_resource_to_user(user_role, resource_id, func.__name__, self)
                    return resource_id
                return func(self, *args, **kw)
            raise MlflowException('Access Denied for {} function'.format(func.__name__), error_code=PERMISSION_DENIED)
    return wrapper


def decorate_all_functions(function_decorator):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                try:
                    obj = obj.__func__  # unwrap Python 2 unbound method
                except AttributeError:
                    pass  # not needed in Python 3
                setattr(cls, name, function_decorator(obj))
        return cls
    return decorator
