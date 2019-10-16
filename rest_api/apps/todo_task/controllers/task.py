from flask import current_app


class TaskDetailController:

    @classmethod
    def delete_task(cls, task_id):
        task_repo = current_app.blueprints['tasks'].repositories.TaskRepository
        task_obj_id = task_repo.delete_task(task_id=task_id)
        return task_obj_id

    @classmethod
    def finish_task(cls, task_id, finished):
        task_repo = current_app.blueprints['tasks'].repositories.TaskRepository
        task_repo.edit_task(task_id=task_id, finished=finished)
        return task_id

    @classmethod
    def edit_task(cls, task_id, name, description, finished):
        task_repo = current_app.blueprints['tasks'].repositories.TaskRepository
        task_repo.edit_task(
            task_id=task_id,
            name=name,
            description=description,
            finished=finished
        )
        return task_id

    @classmethod
    def create_task(cls, name, description, list_id):
        task_repo = current_app.blueprints['tasks'].repositories.TaskRepository
        task_obj_id = task_repo.create_task(name=name, description=description, list_id=list_id)
        return task_obj_id
