from mlflow.entities._mlflow_object import _MLflowObject


class User(_MLflowObject):
    """
    User object to be used in authentication for fetching the roles assigned to a given user.
    On register a user is created in the database and roles are assigned to the user.
    """

    def __init__(self, id, username, password, role, creation_time=None, last_update_time=None):
        super().__init__()
        self._id = id
        self._username = username
        self._password = password
        self._role = role
        self._creation_time = creation_time
        self._last_update_time = last_update_time

    @property
    def id(self):
        """id of the user"""
        return self._id

    @property
    def username(self):
        """String username of the user."""
        return self._username

    @property
    def password(self):
        """String password of the user."""
        return self._password

    @property
    def role(self):
        """String role of the user"""
        return self._role

    @property
    def creation_time(self):
        return self._creation_time

    def _set_creation_time(self, creation_time):
        self._creation_time = creation_time

    @property
    def last_update_time(self):
        return self._last_update_time

    def _set_last_update_time(self, last_update_time):
        self._last_update_time = last_update_time
