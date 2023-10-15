from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User  # Replace 'User' with your user model if it's different
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
