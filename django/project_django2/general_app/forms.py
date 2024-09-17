from django import forms
from .models import CustomUser    

# class RegistrationForm(forms.ModelForm):
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password2 = cleaned_data.get("password2")

#         if password != password2:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data


# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

