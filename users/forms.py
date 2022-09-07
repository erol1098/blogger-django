from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ("avatar", "bio")

class UserForm(UserCreationForm):
  class Meta:
  
    fields = "__all__"