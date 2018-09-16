from django.db import models


class Marker(models.Model):
    name = models.CharField(max_length=35, verbose_name="Název")
    description = models.CharField(max_length=35, verbose_name="Popis")
    long = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Zeměpisná délka")
    lat = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Zeměpisná šířka")
    image = models.URLField(verbose_name="URL adresa ubrázku")
    infocard = models.URLField(verbose_name="URL adresa infokarty")
