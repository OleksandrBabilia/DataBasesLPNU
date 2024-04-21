from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=255)
    phone = models.CharField(15)
