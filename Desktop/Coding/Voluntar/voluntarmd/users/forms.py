from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    name = forms.CharField(max_length=30)
    details = forms.CharField(max_length=500, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ['username','name', 'email', 'password1', 'password2', 'details']