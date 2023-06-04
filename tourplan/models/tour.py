from django.db import models
from django.utils.text import slugify


class Places(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField
    cover_photo = models.ImageField(upload_to='cover/', validators=[])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

