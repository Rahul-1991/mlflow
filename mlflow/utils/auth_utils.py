import jwt
from mlflow.utils.constants import *
from mlflow.exceptions import MlflowException, PERMISSION_DENIED


def get_decrypted_jwt_data(token):
    """
    :param token: String - access token containing information about the user
    :return: dict - Decoded token data
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ENCRYPTION_ALGORITHM])
    except Exception as e:
        raise MlflowException('Invalid jwt token', error_code=PERMISSION_DENIED)


def get_authorised_teams(token):
    """
    :param token:  String - access token containing information about the user
    :return: list - list of teams which the user is a part of.
    """
    decoded_token_data = get_decrypted_jwt_data(token)
    return [team.get('team_id') for team in decoded_token_data.get('teams', list())]
