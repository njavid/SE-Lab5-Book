from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4)))
