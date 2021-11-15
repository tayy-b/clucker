from django.core.validators import RegexValidator
from django import forms
from .models import User
from .models import Post
from django.utils.timezone import datetime


class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message='Password must contain an uppercase character, a lowercase character and a number'
        )]
    )
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())


    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
        self.cleaned_data.get('username'),
        first_name = self.cleaned_data.get('first_name'),
        last_name = self.cleaned_data.get('last_name'),
        email = self.cleaned_data.get('email'),
        bio = self.cleaned_data.get('bio'),
        password = self.cleaned_data.get('new_password'),
        )
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        readonly_fields = ('created_at')
        widgets = {
            'text':forms.Textarea(),
            'created_at':forms.DateTimeInput()}    #'created_at':DateTimeWidget(attr={'id': 'created_at'})


    def save(self, request):
        super().save(commit=False)
        selfpost = Post.objects.create(
        author =request.user,
        text= self.cleaned_data.get('text'),
        created_at = datetime.now())

        username = request.user.username
        text = self.cleaned_data.get('text')
        time = datetime.now()
        # request.user.is_authenticated:
        print(username, text, time)
