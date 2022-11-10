from django.urls import path

from TaskManager.views import index

urlpatterns = [
    path("", index, name="index"),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
    # path(""),
]

app_name = "TaskManager"
