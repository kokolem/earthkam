# Generated by Django 2.1.1 on 2018-09-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Název')),
                ('description', models.CharField(max_length=35, verbose_name='Popis')),
                ('long', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Zeměpisná délka')),
                ('lat', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Zeměpisná šířka')),
                ('image', models.URLField(verbose_name='URL adresa obrázku 752x482')),
                ('fullImage', models.URLField(verbose_name='URL adresa obrázku 4312x2868')),
                ('infocard', models.URLField(verbose_name='URL adresa infokarty')),
            ],
        ),
    ]