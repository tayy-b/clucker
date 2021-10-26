from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from .managers import CategoryManager, PostManager


# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex = r'^@\w{3,}$',
            message = 'Username must consist of....'
        )]
    ) #enforces length constraint
    first_name = models.CharField(max_length=50, blank =False)
    last_name = models.CharField(max_length=50, blank =False)
    email = models.EmailField(unique=True,blank = False)
    bio = models.CharField(max_length=520, blank = True)

class Post(models.Model):
    #many posts can be written by one user
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = User.username
    text = models.CharField(max_length = 280, blank = True)
    #created_at = models.DateTimeField(auto_now_add=True)
    objects = PostManager()
    class Meta: #metadata is anything thats not a field, such as ordering options
        ordering = ['-created_at']
