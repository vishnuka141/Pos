from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class SigninForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

