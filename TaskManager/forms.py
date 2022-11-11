
from django.contrib.auth.forms import UserCreationForm

from TaskManager.models import Worker


class UsersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )
