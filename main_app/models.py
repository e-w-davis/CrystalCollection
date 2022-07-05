from operator import mod
from unicodedata import name
from django.db import models

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    hardness = models.IntegerField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name