from django.urls import path
from .app import get_task_list, get_task_detail, create_task, update_task, delete_task

urlpatterns = [
    path("tasks/", get_task_list, name="task-list"),
    path("tasks/<int:pk>/", get_task_detail, name="task-detail"),
    path("tasks/create/", create_task, name="task-create"),
    path("tasks/<int:pk>/update/", update_task, name="task-update"),
    path("tasks/<int:pk>/delete/", delete_task, name="task-delete"),
]
