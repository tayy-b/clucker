from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    #define different fields as attributes and construct form field objects using clsses predefined.
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','bio']
        widgets = {'bio': forms.Textarea()}

    new_password = forms.CharField(label ="Password", widget = forms.PasswordInput())
    password_confirmation = forms.CharField(label ="Password confirmation", widget = forms.PasswordInput())
