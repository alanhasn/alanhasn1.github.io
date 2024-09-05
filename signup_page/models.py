# accounts/models.py
from django.db import models

class Acounts(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store a hashed password

    def __str__(self):
        return self.username