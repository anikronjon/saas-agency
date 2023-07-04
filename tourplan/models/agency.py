from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=120)
    details = models.TextField()
    weblink = models.URLField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='agency/')

    def __str__(self):
        return self.name

