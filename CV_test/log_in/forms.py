from django.contrib.auth.forms import UserCreationForm

from .models import auth
from main.models import User
from django.forms import ModelForm, TextInput

class authForm(ModelForm):
    class Meta:
        model = auth
        fields = ['login', 'password']

        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'login'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            })
        }

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
