from django.db import models

# Create your models here.
class Books(models.Model):
    TITLE = models.CharField(max_length=52)
    AUTHOR = models.CharField(max_length=52)
    YEAR = models.CharField(max_length=52)
    IBN =  models.CharField(max_length=52) 