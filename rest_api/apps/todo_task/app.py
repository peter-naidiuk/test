from rest_api.utils.base_blueprint import BaseBlueprint
from .controllers import CONTROLLERS
from .repositories import REPOSITORIES
from .urls import urls


class TaskBlueprint(BaseBlueprint):
    _url_prefix = "/tasks"
    _controllers = CONTROLLERS
    _repositories = REPOSITORIES
    _urls = urls
