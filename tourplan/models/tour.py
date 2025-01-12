from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .address import Location


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class TourPlace(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
    address = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='tourplaces')
    name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(max_length=120, unique=True)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    cover_photo = models.ImageField(upload_to='cover/', validators=[])
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tourplan:tourplan_detail_page', args=[self.slug])



