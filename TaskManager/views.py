from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from TaskManager.forms import WorkerCreationForm, WorkerUpdateForm, TaskCreateForm, TaskUpdateForm

from TaskManager.models import Worker, Task


@login_required
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
    form_class = WorkerCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy('TaskManager:done')

    def get_success_url(self):
        return reverse_lazy("TaskManager:done", kwargs={"name": self.object.username})


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "TaskManager/worker_list.html"
    paginate_by = 2


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "account/worker_detail.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy('TaskManager:worker_detail')
    template_name = "account/worker_update.html"

    def get_success_url(self):
        return reverse_lazy("TaskManager:worker_detail", kwargs={"slug": self.object.slug})


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("TaskManager:index")
    template_name = "account/worker_delete.html"


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"

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


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "TaskManager/task_list.html"
    paginate_by = 5


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "TaskManager/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("TaskManager:tasks-detail")
    template_name = "TaskManager/task_update.html"

    def get_success_url(self):
        return reverse_lazy("TaskManager:tasks-detail", kwargs={"pk": self.object.id})


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "TaskManager/task_create.html"
    success_url = reverse_lazy("TaskManager:tasks-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "TaskManager/confirm_delete_task.html"
    success_url = reverse_lazy("TaskManager:tasks-list")


@login_required
def task_complete_view(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("TaskManager:tasks-list"))
