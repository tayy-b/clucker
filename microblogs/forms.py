from django import forms
from .models import User,Post
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    #define different fields as attributes and construct form field objects using clsses predefined.
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','bio']
        widgets = {'bio': forms.Textarea()}

    new_password = forms.CharField(
        label ="Password",
        widget = forms.PasswordInput(),
        validators=[ RegexValidator(
            regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message = 'Password must contain upper,lower numbers..'
        )
        ]
    )
    password_confirmation = forms.CharField(label ="Password confirmation", widget = forms.PasswordInput())

    #override clean method

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation =  self.cleaned_data.get('password_confirmation')

        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password')

    def save(self):
        super().save(commit = False) #save method wont store the record in the data base
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            email = self.cleaned_data.get('email'),
            bio = self.cleaned_data.get('bio'),
            password = self.cleaned_data.get('new_password')
        )
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {'text':forms.Textarea()}

    def printText(self):
        super().save(commit = False)
        text = self.cleaned_data.get('text')
        print(text)
