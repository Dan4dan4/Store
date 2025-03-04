from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=75)
    description= models.CharField(max_length=1000)
    price= models.IntegerField()
    quantity= models.IntegerField()
    material= models.CharField(max_length=200)

    def __str__(self):
        return (f"ID:#{self.id}: {self.title}, {self.description},price:${self.price}, quantity:{self.quantity},material:{self.material}")