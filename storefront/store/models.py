from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=75)
    description= models.CharField(max_length=1000)
    price= models.IntegerField()
    quantity= models.IntegerField()
