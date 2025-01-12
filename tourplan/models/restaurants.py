from django.db import models
from .address import Location


class Restaurant(models.Model):
    RATING_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    name = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    address = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='restaurants')
    weblink = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=120)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='restaurants/')


    def __str__(self):
        return self.name
