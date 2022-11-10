from django.shortcuts import render

from TaskManager.models import Worker, Task


def index(request):
    """View function for the home page of the site."""
    num_workers = Worker.objects.count()
    num_task = Task.objects.count()

    context = {
        "num_workers": num_workers,
        "num_task": num_task
    }
    return render(request, "TaskManager/index.html", context=context)


