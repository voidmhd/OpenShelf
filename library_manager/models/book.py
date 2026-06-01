from django.db import models

from library_manager.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    published_date = models.DateField(verbose_name="Published Date")
    isbn = models.CharField(max_length=13, verbose_name="ISBN")
    authors = models.ManyToManyField(Author, verbose_name="Authors")
