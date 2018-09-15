from django.db import models


class Marker(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=35)
    long = models.DecimalField(decimal_places=2, max_digits=5)
    lat = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.URLField()
    infocard = models.URLField()
