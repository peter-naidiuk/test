from flask import current_app


class ListSetController:

    @classmethod
    def create_list(cls, name):
        list_repo = current_app.blueprints['lists'].repositories.ListRepository
        list_obj_id = list_repo.create_list(name=name)
        return list_obj_id

    @classmethod
    def get_lists(cls):
        list_repo = current_app.blueprints['lists'].repositories.ListRepository
        lists = list_repo.get_all_lists()
        return lists


class ListDetailController:

    @classmethod
    def get_list(cls, list_id):
        list_repo = current_app.blueprints['lists'].repositories.ListRepository
        lists = list_repo.get_list_by_id(list_id=list_id)
        return lists

    @classmethod
    def get_tasks_from_list(cls, list_id):
        task_repo = current_app.blueprints['tasks'].repositories.TaskRepository
        tasks = task_repo.get_all_task_from_list(list_id=list_id)
        return tasks
