from django.db import models
from authors.models import Author
from publishers.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=55)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    price = models.FloatField()
    author = models.ManyToManyField(Author)
    publisher= models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    cover = models.ImageField()
    about = models.TextField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-title"]

    def __str__(self):
        return f"{self.title}" 

