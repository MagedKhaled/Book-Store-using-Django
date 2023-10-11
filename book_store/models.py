from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    inStock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

        
    