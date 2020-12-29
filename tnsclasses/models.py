from django.db import models
import datetime


class Day(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    class_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class TNS_Class(models.Model):
    class Meta:
        verbose_name_plural = 'TNS Class'

    day = models.ForeignKey('Day', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    class_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name