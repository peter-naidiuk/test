from rest_api.utils.url_rule import UrlRule
from .views import ListSetView, ListDetailView, ListTasksDetailView

urls = [
    UrlRule(path="/", dispatcher=ListSetView.as_view("lists")),
    UrlRule(path="/<int:list_id>", dispatcher=ListDetailView.as_view("list_detail")),
    UrlRule(path="/<int:list_id>/tasks", dispatcher=ListTasksDetailView.as_view("list_detail_tasks")),
]
