from django.test import TestCase
from microblogs.forms import SignUpForm
from django.urls import reverse


class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.url =  reverse('sign_up')
        self.form_input = {
        'first_name': 'Jane',
        'last_name': 'DOe',
        'username': '@janedoe',
        'email': 'janedoe@gmail.com',
        'bio': 'yadaydayda',
        'new_password':'Password123',
        'password_confirmation':'Password123'
        }


    def test_getsignup(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsuccesfful(self):
        self.form_input['username'] = 'BAD_USERNAME'
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)
