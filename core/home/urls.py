from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('',get_post_method),
   path('view', view),
   path('user',get_user_data)
]
