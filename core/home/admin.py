from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *

admin.site.register(UserDetails)

# models = apps.get_models()

# for model in models:
#     admin.site.register(model)