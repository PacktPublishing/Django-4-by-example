from django import forms
from django.contrib.auth.models import User                                    # new


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):                                   # new
    password = forms.CharField(label='Password',                               # new
                               widget=forms.PasswordInput)                     # new
    password2 = forms.CharField(label='Repeat password',                       # new
                                widget=forms.PasswordInput)                    # new

    class Meta:                                                                # new
        model = User                                                           # new
        fields = ['username', 'first_name', 'email']                           # new
