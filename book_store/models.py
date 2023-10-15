from django.db import models
from category.models import Category
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):

    owner = models.ForeignKey(User,
                            on_delete=models.CASCADE, related_name='owned_objects')

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_store/images/',max_length=200)
    price = models.IntegerField()
    inStock = models.IntegerField(default=0)

    category = models.ForeignKey(Category, null=True, blank=True,
                            on_delete=models.CASCADE, related_name='book_store')

    def __str__(self):
        return self.name


    def get_image_url(self):
        return f"/media/{self.image}"
    
    def get_show_url(self):
        return  reverse('book_store.details', args=[self.id])

    def get_edit_url(self):
        return  reverse('book_store.edit', args=[self.id])

    def get_delete_url(self):
        return  reverse('book_store.delete', args=[self.id])
