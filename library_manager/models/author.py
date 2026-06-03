from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    age = models.IntegerField(verbose_name="Age")
    # number_of_published_books = models.IntegerField(
    #     verbose_name="Number of Publications"
    # )
