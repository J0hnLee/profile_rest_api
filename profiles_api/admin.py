from django.contrib import admin
from profiles_api import models


# Register your models here.

'''Make it access through django admin interface'''
admin.site.register(models.UserProfile)
