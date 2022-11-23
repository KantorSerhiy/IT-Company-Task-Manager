from django import forms
from django.contrib.auth.forms import UserCreationForm

from TaskManager.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "position"
        )


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "is_completed", "assignees", "deadline", "priority"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "is_completed", "assignees", "deadline", "priority"]


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]
