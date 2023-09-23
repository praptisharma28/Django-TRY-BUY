from django import forms   
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.models import Login,Signup
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Signup
        fields = ['Username', 'Password', 'Confirm_Password']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Login
        fields = ['Username', 'Password']
