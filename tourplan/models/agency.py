from django.db import models


class Agency(models.Model):
    name = models.CharField()
    details = models.TextField()
    rating = models.IntegerField()
    web_link = models.URLField()

    def __str__(self):
        return self.name

