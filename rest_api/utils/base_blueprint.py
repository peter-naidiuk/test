from flask import Blueprint

from .controllers_registry import ControllerRegistry
from .repositories_registry import RepositoryRegistry


class BaseBlueprint(Blueprint):
    _controllers = None
    _repositories = None
    _urls = None
    _url_prefix = None

    def __init__(self, name, import_name, **kwargs):
        super().__init__(name, import_name, **kwargs)
        self.controllers = self.__setup_controllers()
        self.repositories = self.__setup_repositories()
        self.__setup_urls()
        self.url_prefix = self._url_prefix

    def __setup_urls(self):
        for url_rule in self._urls:
            self.add_url_rule(url_rule.path, view_func=url_rule.dispatcher)

    def __setup_controllers(self):
        controllers_registry = ControllerRegistry()
        for controller in self._controllers:
            controllers_registry.add_controller(controller)
        return controllers_registry

    def __setup_repositories(self):
        return RepositoryRegistry(self._repositories)
