from mlflow.entities._mlflow_object import _MLflowObject


class Entitlement(_MLflowObject):
    """
    Entitlement object which contains permissions of team of which a user can be a part of.
    """

    def __init__(self, entitlement_id: int, team_id: int, team_name: str, permissions: dict, creation_time=None, last_update_time=None):
        super().__init__()
        self._entitlement_id = entitlement_id
        self._team_id = team_id
        self._team_name = team_name
        self._permissions = permissions
        self._creation_time = creation_time
        self._last_update_time = last_update_time

    @property
    def entitlement_id(self):
        return self._entitlement_id

    @property
    def team_id(self):
        return self._team_id

    @property
    def team_name(self):
        return self._team_name

    @property
    def permissions(self):
        return self._permissions

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
