from django import forms
from django.db import models
from django.conf import settings


class NameForm(forms.Form):
    """
    This form allow the user to enter the name of an other user that he
    wants to follow.
    """
    name = forms.CharField(max_length=128, label='')
