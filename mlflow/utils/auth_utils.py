import jwt
import inspect
from flask import request
from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import PERMISSION_DENIED
from mlflow.utils.user_role_access import role_access_map
from mlflow.utils.constants import ACTIONS, DEFAULT_ALLOCATED_ROLE, SYSTEM_ADMIN_ROLE, JWT_SECRET_KEY, JWT_ENCRYPTION_ALGORITHM


def assign_resource_to_user(user_role, resource_id, func_name, class_obj):
    """
    This function allocates the resource id of the created resource to the DEFAULT_ALLOCATED_ROLE for the user.
    """
    for action in ACTIONS:
        if action in func_name:
            if not user_role.get(DEFAULT_ALLOCATED_ROLE):
                user_role.update({DEFAULT_ALLOCATED_ROLE: {action: [resource_id]}})
            else:
                accessible_resources = user_role.get(DEFAULT_ALLOCATED_ROLE, {}).get(action)
                accessible_resources.append(resource_id)
                user_role.get(DEFAULT_ALLOCATED_ROLE).update({action: accessible_resources})
        with class_obj.ManagedSessionMaker() as session:
            session.query(SqlUser).filter(SqlUser.id == resource_id).update({'role': json.dumps(user_role)})
            session.flush()


def _user_has_access(user_role, user_action, resource):
    """
    returns if the user has access to the given resource id by checking in the assigned resources
    """
    for role, access in user_role.items():
        for action, resource_list in access.items():
            if action == user_action and (not resource or resource in resource_list):
                return True
    return False


def _get_user_permissions(user_role):
    """
    returns list of all resources assigned to user in different roles
    """
    return set([access for role, access_data in user_role.items() if role_access_map.get(role)
            for access in role_access_map.get(role)])


def is_operation_allowed(user_role, func_name, func_params):
    """
    checks if user is allowed to perform the operation based on his role
    """
    if SYSTEM_ADMIN_ROLE in user_role:
        return True
    for permission in _get_user_permissions(user_role):
        if permission in ['get']:
            for action in ACTIONS:
                if permission in func_name:
                    return _user_has_access(user_role, action, func_params)
        else:
            if permission in func_name:
                return True
    return False


def get_decrypted_jwt_data(token):
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ENCRYPTION_ALGORITHM])
    except Exception as e:
        raise MlflowException('Invalid jwt token', error_code=PERMISSION_DENIED)
