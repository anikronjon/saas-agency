from django.db import models
from .address import Location

class Hotel(models.Model):
    name = models.CharField(max_length=120)
    details = models.CharField(max_length=200)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotels')
    weblink = models.URLField()
    image = models.ImageField(upload_to='hotel/')

    def __str__(self):
        return self.name


