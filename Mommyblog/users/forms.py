from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ new registration fields to U.C.form"""
    email = forms.EmailField()

    class Meta:
        """model to interact"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
