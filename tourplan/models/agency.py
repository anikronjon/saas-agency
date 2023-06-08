from django.db import models


class Agency(models.Model):
    name = models.CharField()
    details = models.TextField()
    web_link = models.URLField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

