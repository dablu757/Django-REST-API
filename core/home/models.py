from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 100)


class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 18)
    father_name = models.CharField(max_length = 100)


class Category(models.Model):
    category_name = models.CharField(max_length = 100)


class Books(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    book_tiltle = models.CharField(max_length = 100)

