from django.test import TestCase
from microblogs.models import User, Post
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

    def test_firstname_cant_be_blank(self):
        self.user.first_name = ""
        self._assert_user_is_invalid()


    def _create_second_user(self):
        user = User.objects.create_user(
            '@mushiddin',
            first_name ='Mushi',
            last_name="Uddin",
            email="mushiuddin@gmail.com",
            password="Password123",
            bio="heloooo im mushi"
        )
        return user

    def test_username_is_unique(self):
            second_user=self._create_second_user()
            self.user.username=second_user.username
            self._assert_user_is_invalid()

    def test_firstname_neednt_be_unqiue(self):
        second_user=self._create_second_user()
        self.user.first_name=second_user.first_name
        self._assert_user_is_valid()

    def test_firstname_cant_be_more_than_50_characters_long(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()


    def test_lastname_cant_be_blank(self):
        self.user.last_name = ""
        self._assert_user_is_invalid()

    def test_lastname_neednt_be_unqiue(self):
        second_user=self._create_second_user()
        self.user.last_name=second_user.last_name
        self._assert_user_is_valid()

    def test_lastname_can_be_50_characters_long(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()

    def test_username_cannot_be_50_characters_long(self):
        self.user.username = 'x' * 51
        self._assert_user_is_invalid()

    def test_email_cant_be_blank(self):
        self.user.email= ""
        self._assert_user_is_invalid()


class PostTestCase(TestCase):

    def create_author(self):
        author = User.objects.create_user(
            '@tayyibahuddin',
            first_name ='Tayyibah',
            last_name="Uddin",
            email="taybzz.u.95@gmail.com",
            password="Password123",
            bio="heloooo"
            )
        return author

    def setUp(self):

        self.post = Post.objects.create(
           author = self.create_author(),
           text="heloooo",
       )

    def _assert_post_is_valid(self):
        try:
             self.post.full_clean()
        except(ValidationError):
             self.fail('Test model should be valid.')

    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_valid_post(self):
        self._assert_post_is_valid()

    def test_author_cant_be_blank(self):
        self.post.author = None
        self._assert_post_is_invalid

    def test_text_can_be_280_characters(self):
        self.post.text = 'x' * 280
        self._assert_post_is_valid

    def test_text_cant_be_over_280_characters(self):
        self.post.text = 'x' * 281
        self._assert_post_is_invalid
