from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    series = models.CharField(max_length=40)
    book_type = models.CharField(max_length=40)
    categories = models.CharField(max_length=40)
    lexile_min = models.BigIntegerField
    lexile_max = models.BigIntegerField
    results_per_page = models.IntegerField
    page = models.IntegerField

    def __str__(self):
        return self.title
