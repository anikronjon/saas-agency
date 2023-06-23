from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=120)
    details = models.CharField(max_length=200)
    address = models.CharField(max_length=120)
    weblink = models.URLField()

    def __str__(self):
        return self.name


