from django import forms
from .models import CustomUser, SingUpIUser, SignInIUser
from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']
from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # password = forms.CharField(widget=forms.PasswordInput)
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SingUpIUser
        fields = ['username', 'email', 'password']

class SignInIUser(forms.ModelForm):
    class Meta:
        model = SignInIUser
        fields = ['email', 'password']
    
