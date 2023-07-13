from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    agreed = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'agreed']


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']
