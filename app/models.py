from django.db import models
import datetime as dt

from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length =30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30, blank=False, null=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =20)
    image = CloudinaryField('image')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
