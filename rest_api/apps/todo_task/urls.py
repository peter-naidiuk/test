from rest_api.utils.url_rule import UrlRule
from .views import TaskDetailView

urls = [
    UrlRule("/<int:task_id>", TaskDetailView.as_view("task_detail"))
]
