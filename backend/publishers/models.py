from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=255)
    phone = models.CharField(15)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name}" 

