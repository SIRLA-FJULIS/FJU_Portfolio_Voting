from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('studID', 'fullName', 'department', 'is_active') #, 'is_admin'