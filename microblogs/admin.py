"""Configuration of the administrative interface for microblogs."""
from django.contrib import admin
from .models import User

@admin.register(User)
#@admin.register(Post)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""
    list_display = [
        'username','first_name','last_name','email','is_active',
    ]
