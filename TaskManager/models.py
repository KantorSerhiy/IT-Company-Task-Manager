from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}"


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=63, unique=True)

    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)

        return super(Worker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            "slug": self.slug
        }
        return reverse('TaskManager:worker_detail', kwargs=kwargs)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username}({self.first_name} {self.last_name})"

    objects = UserManager()


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("U", "Urgent"),
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=Worker, related_name="tasks")
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["is_completed", "created_ad"]

    def __str__(self):
        return f"{self.name}( type:{self.task_type},priority {self.priority})"
