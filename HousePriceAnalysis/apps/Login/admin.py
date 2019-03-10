from django.contrib import admin

# Register your models here.
from apps.Login import models
admin.site.register(models.User)