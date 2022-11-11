from django.urls import path

from TaskManager.views import index, RegisterUser, LoginUser, LogoutUser, RegisterDone

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("done/<str:name>", RegisterDone.as_view(), name="done"),
]

app_name = "TaskManager"
