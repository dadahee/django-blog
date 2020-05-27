from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        birthday = forms.DateField(input_formats=['%Y/%m/%d'])
        fields = [ "username", "password1", "password2", "profile", "email", "birthday", "gender" ]