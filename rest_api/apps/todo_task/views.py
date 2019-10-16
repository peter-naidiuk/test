from http import HTTPStatus

from flask import request, current_app
from marshmallow import ValidationError

from rest_api.utils.base_view import BaseView
from .schemas import TaskPatchSchema, TaskEditSchema


class TaskDetailView(BaseView):

    def delete(self, task_id):
        current_app.blueprints['tasks'].controllers.TaskDetailController.delete_task(
            task_id=task_id,
        )
        return self.get_response("OK", status=HTTPStatus.OK)

    def patch(self, task_id):
        try:
            data = TaskPatchSchema().load(request.json)
        except ValidationError:
            raise Exception("Bad request")
        modified_data = current_app.blueprints['tasks'].controllers.TaskDetailController.finish_task(
            task_id=task_id,
            finished=data.get("finished")
        )
        return self.get_response(modified_data, status=HTTPStatus.OK)

    def put(self, task_id):
        try:
            data = TaskEditSchema().load(request.json)
        except ValidationError:
            raise Exception("Bad request")
        modified_data = current_app.blueprints['tasks'].controllers.TaskDetailController.edit_task(
            task_id=task_id,
            name=data.get("name"),
            description=data.get("description"),
            finished=data.get("finished")
        )
        return self.get_response(modified_data, status=HTTPStatus.OK)
