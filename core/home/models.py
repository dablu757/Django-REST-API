from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 100)
