from django.forms import ModelForm
from .models import State, User, City


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'hometown', 'state_hometown', 'regenerate_map']
