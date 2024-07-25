from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('',get_post_method),
   path('view', view),
   path('user',get_user_data),
   path('create_user',create_user),
   path('user-update/<id>/' ,update_user_details),
   path('user-delete/', delete_user),
]
