from django.contrib import admin

# Register your models here.
from Route import models
admin.site.register(models.routes)