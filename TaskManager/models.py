from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return {self.name}


class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return {self.name}


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=63, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)

        return super(Worker, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username}({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY_CHOISES = [
        ("U", "Urgent"),
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOISES)
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=Worker, related_name="tasks")
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}( type:{self.task_type},deadline{self.deadline}, priority{self.priority})"
