from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('username', 'email')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields