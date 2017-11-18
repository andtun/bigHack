from django.db import models

__all__ = ['Building']


class Building(models.Model):
    address = models.CharField('адрес', max_length=1024)
    license = models.CharField('лицензия', max_length=128)
    square = models.FloatField('площадь')
    historic = models.BooleanField('историческое значение')
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')

    class Meta:
        verbose_name = 'строение'
        verbose_name_plural = 'строения'
