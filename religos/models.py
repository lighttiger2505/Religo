from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
