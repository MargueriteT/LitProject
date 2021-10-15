from django import forms
from django.db import models
from django.conf import settings


class NameForm(forms.Form):
    name = forms.CharField(max_length=128, label='')
