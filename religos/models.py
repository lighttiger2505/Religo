from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    file = models.FileField(upload_to='photos/%Y/%m/%d')
    ocr_text = models.TextField(max_length=2000)
