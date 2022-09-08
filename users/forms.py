from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ("avatar", "bio")

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


class UpdateUserProfileForm(UserChangeForm):
  class Meta:
    model = User
    fields = ("username", "email")