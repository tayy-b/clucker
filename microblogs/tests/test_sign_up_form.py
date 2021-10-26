from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User
from django import forms


class SignUpFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
        'first_name': 'Jane',
        'last_name': 'DOe',
        'username': '@janedoe',
        'email': 'janedoe@gmail.com',
        'bio': 'yadaydayda',
        'new_password':'Password123',
        'password_confirmation':'Password123'
        }

    def test_valid_signupform(self):
        form = SignUpForm(data = self.form_input)
        self.assertTrue(form.is_valid())


    def test_formhasnecessaryfields(self):
        form = SignUpForm()
        self.assertIn('first_name',form.fields) #checks theres an item in the dictionary
        self.assertIn('last_name',form.fields) #checks theres an item in the dictionary
        self.assertIn('username',form.fields) #checks theres an item in the dictionary
        self.assertIn('email',form.fields) #checks theres an item in the dictionary
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field,forms.EmailField))
        self.assertIn('bio',form.fields) #checks theres an item in the dictionary
        self.assertIn('new_password',form.fields) #checks theres an item in the dictionary
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation',form.fields) #checks theres an item in the dictionary
        password_confirmation_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))

    def test_form_usesmodelvalidation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())
