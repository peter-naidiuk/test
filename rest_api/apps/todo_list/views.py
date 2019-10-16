from http import HTTPStatus

from flask import current_app
from flask import request

from rest_api.utils.base_view import BaseView
from .schemas import ListCreateSchema, TaskCreateSchema


class ListSetView(BaseView):

    def get(self):
        data = current_app.blueprints['lists'].controllers.ListSetController.get_lists()
        return self.get_response(data)

    def post(self):
        data = self.validate_request(request.json, ListCreateSchema)
        list_id = current_app.blueprints['lists'].controllers.ListSetController.create_list(name=data['name'])
        return self.get_response(list_id, status=HTTPStatus.CREATED)


class ListDetailView(BaseView):

    def get(self, list_id):
        data = current_app.blueprints['lists'].controllers.ListDetailController.get_list(list_id=list_id)
        return self.get_response(data)


class ListTasksDetailView(BaseView):

    def get(self, list_id):
        data = current_app.blueprints['lists'].controllers.ListDetailController.get_tasks_from_list(list_id=list_id)
        return self.get_response(data)

    def post(self, list_id):
        data = self.validate_request(request.json, TaskCreateSchema)
        current_app.blueprints['tasks'].controllers.TaskDetailController.create_task(
            name=data.get("name"),
            description=data.get("description"),
            list_id=list_id,
        )
        return self.get_response("OK", status=HTTPStatus.CREATED)
