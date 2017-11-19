from django.db import models

__all__ = ['Building', 'Application', 'Image']


class Building(models.Model):
    address = models.CharField('адрес', max_length=1024)
    license = models.CharField('лицензия', max_length=128)
    square = models.FloatField('площадь')
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')

    class Meta:
        verbose_name = 'строение'
        verbose_name_plural = 'строения'

    __str__ = lambda self: 'Строение @ ' + self.address


class Application(models.Model):
    title = models.CharField('название', max_length=64)
    building = models.ForeignKey(Building, related_name='applications')
    rating = models.IntegerField('рейтинг', blank=True, default=0)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    __str__ = lambda self: 'Заявка на строение #{}'.format(self.building.pk)


class Image(models.Model):
    application = models.ForeignKey(Application, related_name='images')
    file = models.ImageField('файл', blank=False)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    __str__ = lambda self: 'Изображене для заявки #{}'.format(self.application.pk)
