from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    # class Meta(UserCreationForm.Meta):
    #     fields = UserCreationForm.Meta.fields + ('email',)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #     email = cleaned_data.get("email")

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")

    #     existing_user = CustomUser.objects.filter(email=email).first()
    #     if existing_user:
    #         self.existing_user = existing_user
    #         raise forms.ValidationError("This email is already registered.")

    #     return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)