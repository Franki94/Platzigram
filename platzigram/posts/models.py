"""Posts models."""

#Django
from django.db import models

class User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 100)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    is_admin = models.BooleanField(default=False)

    country = models.CharField(max_length = 50, null = True)
    city = models.CharField(max_length = 50, null = True)

    bio = models.TextField()

    birth_date = models.DateField(blank = True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.email
