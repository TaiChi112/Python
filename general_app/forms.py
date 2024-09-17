from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    # hiding password field
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # using custom user model from models.py
        model = CustomUser
        fields = ['username', 'email', 'password']

class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)