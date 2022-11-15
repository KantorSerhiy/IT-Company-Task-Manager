from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from TaskManager.forms import UsersCreationForm

from TaskManager.models import Worker, Task


def index(request):
    """View function for the home page of the site."""
    num_workers = Worker.objects.count()
    num_task = Task.objects.count()

    context = {
        "num_workers": num_workers,
        "num_task": num_task,
    }
    return render(request, "TaskManager/index.html", context=context)


class RegisterUser(generic.CreateView):
    model = Worker
    form_class = UsersCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy('TaskManager:done')

    def get_success_url(self):
        return reverse_lazy("TaskManager:done", kwargs={"name": self.object.username})


class UserDetailView(generic.DetailView):
    model = Worker
    template_name = "account/worker_detail.html"


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "account/login.html"

    def get_success_url(self):
        return reverse_lazy('TaskManager:index')


class LogoutUser(LogoutView):
    template_name = "account/logout.html"


class RegisterDone(LoginView):
    template_name = "account/register_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs["name"]
        return context
