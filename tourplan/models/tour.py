from django.db import models
from django.utils.text import slugify
from .address import Location
from common.validator import image_size_validation, video_size_validation


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    name = models.CharField(max_length=20, unique=True)


class TourPlace(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
    address = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='tourplaces')
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField
    cover_photo = models.ImageField(upload_to='cover/', validators=[])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    tour = models.ForeignKey(TourPlace, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/tour', validators=[image_size_validation(1)])


class Video(models.Model):
    tour = models.ForeignKey(TourPlace, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos/tour', validators=[video_size_validation(5)])
