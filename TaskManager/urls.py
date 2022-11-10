from django.urls import path

from TaskManager.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "TaskManager"
