from django.urls import path

from TaskManager.views import (
    index,
    RegisterUser,
    LoginUser,
    LogoutUser,
    RegisterDone,
    WorkerDetailView,
    WorkerDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("done/<str:name>", RegisterDone.as_view(), name="done"),
    path("worker/<slug:slug>", WorkerDetailView.as_view(), name="worker_detail"),
    path("worker/<slug:slug>/delete/", WorkerDeleteView.as_view(), name="worker-delete")
]

app_name = "TaskManager"
