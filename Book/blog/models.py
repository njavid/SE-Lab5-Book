from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4)),validators=[MaxValueValidator(4), MinValueValidator(1)])
