from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ This form is used to create an account on the web app. """

    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    """ This form is used to update profile picture. """

    class Meta:
        model = Profile
        fields = ['image']

