from .todo_list.app import ListBlueprint
from .todo_task.app import TaskBlueprint

list_app = ListBlueprint("lists", __name__)
task_app = TaskBlueprint("tasks", __name__)

APPS = [
    list_app,
    task_app,
]
