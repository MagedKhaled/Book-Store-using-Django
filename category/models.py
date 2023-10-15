from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_store/images/',max_length=200)

    def __str__(self):
        return self.name
    

    def get_image_url(self):
        return f"/media/{self.image}"
    