from django.db import models


class Marker(models.Model):
    name = models.CharField(max_length=35, verbose_name="Název")
    description = models.CharField(max_length=35, verbose_name="Popis")
    long = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Zeměpisná délka")
    lat = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Zeměpisná šířka")
    image = models.URLField(verbose_name="URL obrázku 752x482")
    fullImage = models.URLField(verbose_name="URL obrázku 4312x2868")
    infocard = models.URLField(verbose_name="URL infokarty")
