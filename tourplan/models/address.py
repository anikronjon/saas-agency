from django.db import models


class Location(models.Model):
    class DivisionChoices(models.TextChoices):
        BARISAL = 'BRS', 'Barisal'
        CHITTAGONG = 'CTG', 'Chittagong'
        DHAKA = 'DHK', 'Dhaka'
        Khulna = 'KLN', 'Khulna'
        MYMENSINGH = 'MMS', 'Mymensingh'
        RAJSHAHI = 'RJS', 'Rajshahi'
        RANGPUR = 'RGP', 'Rangpur'
        SYLHET = 'SYL', 'Sylhet'
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f'{self.division} - {self.district}'

