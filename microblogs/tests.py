from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

# Create your tests here.
class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@tayyibahuddin',
            first_name ='Tayyibah',
            last_name="Uddin",
            email="taybzz.u.95@gmail.com",
            password="Password123",
            bio="heloooo"
        )

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid.')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_username_cant_be_blank(self):
        self.user.username = ""
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_user_is_invalid()


def test_username_is_unique(self):
        User.objects.create_user(
            '@mushiddin',
            first_name ='Mushi',
            last_name="Uddin",
            email="mushiuddin@gmail.com",
            password="Password123",
            bio="heloooo im mushi"
        )

        self.user.username = '@janedoe'
        self._assert_user_is_invalid()
