from django.db import models
from authors.models import Author
from publishers.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=55)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    price = models.FloatField()
    author_id = models.ManyToManyField(Author)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    cover = models.ImageField()
    about = models.TextField()

