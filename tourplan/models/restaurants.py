from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    place = models.CharField(max_length=120)