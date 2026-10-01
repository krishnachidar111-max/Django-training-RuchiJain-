from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    # UserCreationForm already provides password fields, so we only need to specify 'username'
    class Meta:
        model = User
        fields = ['username']