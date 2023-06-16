from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)


