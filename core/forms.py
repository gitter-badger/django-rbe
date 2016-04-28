from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, Textarea, ModelForm
from django.forms.widgets import PasswordInput, EmailInput, TextInput


class RegistrationForm(Form):

    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Sorry this username is already taken!")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Sorry this email is already taken!")

        if password and password_repeat:
            # Only do something if both fields are valid so far.
            if password != password_repeat:
                raise forms.ValidationError("Passwords don't match!")


class LoginForm(Form):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))