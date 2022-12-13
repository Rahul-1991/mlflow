import inspect
from flask import request
from functools import wraps
from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import PERMISSION_DENIED
from mlflow.utils.auth_utils import is_operation_allowed, assign_resource_to_user, get_decrypted_jwt_data


def perform_authorization(func):
    @wraps(func)
    def wrapper(self, *args, **kw):
        jwt_data = get_decrypted_jwt_data(request.headers.get('jwt'))
        try:
            user_role = json.loads(jwt_data.get('role'))
        except Exception as e:
            user_role = dict()
        # user_role = {'PV': {'experiment': ["exp2", "exp3"]}}
        if func.__name__.startswith('_'):
            return func(self, *args, **kw)
        func_arguments, variable_arguments, keywords, defaults = inspect.getargspec(func)
        experiment_param = None
        for index, param in enumerate(func_arguments):
            if param == 'experiment_id' or param == 'experiment_name':
                experiment_param = args[index - 1]
        if is_operation_allowed(user_role, func.__name__, experiment_param):
            if 'create' in func.__name__:
                resource_id = func(self, *args, **kw)
                assign_resource_to_user(user_role, resource_id, func.__name__, self)
                return resource_id
            return func(self, *args, **kw)
        raise MlflowException('Access Denied for {} function'.format(func.__name__), error_code=PERMISSION_DENIED)
    return wrapper


def authorise_class_methods():
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                setattr(cls, name, perform_authorization(obj))
        return cls
    return decorator
