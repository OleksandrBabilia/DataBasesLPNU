from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=75)
    bio = models.TextField()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["-first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

