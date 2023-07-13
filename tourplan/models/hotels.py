from django.db import models
from django.utils.text import slugify
from .address import Location


class Hotel(models.Model):
    RATING_STATUS = (
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    details = models.CharField(max_length=200)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotels')
    rating = models.IntegerField(choices=RATING_STATUS)
    weblink = models.URLField()
    image = models.ImageField(upload_to='hotel/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
