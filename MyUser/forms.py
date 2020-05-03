from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
	
	class Meta:
		model = get_user_model()
		fields = ('email', 'password')