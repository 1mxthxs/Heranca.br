from django import forms 
from allauth.account.forms import LoginForm, SignupForm

class CustomLoginForm(LoginForm):
    email = forms.EmailField(label=("Email"))
    
class CustomSignupForm(SignupForm):
    email = forms.EmailField(
        max_length=254,
        label="Email",
        widget=forms.EmailInput(attrs={'type': 'email'}),
        required=True)
    