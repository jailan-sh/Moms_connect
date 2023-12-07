from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ new registration fields to U.C.form"""
    email = forms.EmailField()

    class Meta:
        """model to interact"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """ update user info."""
    email = forms.EmailField()

    class Meta:
        """ model to update"""
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """ to upsate profile information"""
    Bio = forms.CharField(max_length=1000, required=False)
    class Meta:
        """MODEL TO UPDATE"""
        model = Profile
        fields = ['image', 'Bio']
