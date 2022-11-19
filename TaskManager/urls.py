from django.urls import path

from TaskManager.views import (
    index,
    RegisterUser,
    LoginUser,
    LogoutUser,
    RegisterDone,
    WorkerDetailView,
    WorkerDeleteView,
    WorkerUpdateView,
    WorkerListView,
    TaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    task_complete_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("done/<str:name>", RegisterDone.as_view(), name="done"),
    path("worker/<slug:slug>", WorkerDetailView.as_view(), name="worker_detail"),
    path("workers/", WorkerListView.as_view(), name="worker_list"),
    path("worker/<slug:slug>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("worker/<slug:slug>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/", TaskDeleteView.as_view(), name="tasks-delete"),
    path("tasks/complate/<int:pk>", task_complete_view, name="task-complete")
]

app_name = "TaskManager"
