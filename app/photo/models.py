from django.db import models
from django.conf import settings


class Country(models.Model):
    '''
    Страна, где фото было снято
    '''
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    '''
    Город, где фото было снято
    '''
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name} ({self.country})'


class Thing(models.Model):
    '''
    то что было снято на фото 
    '''
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return f'{self.name}'


class Photo(models.Model):
    '''
    вся информация о фото:
    - заголовок
    - автор, кто загрузил фото
    - одобрена ли фото
    - кем одобрена
    - город, страна где было сделано фото
    - вещи, которые есть на фото
    '''
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    accepted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)
    things = models.ManyToManyField(Thing, null=True, blank=True)
    image = models.ImageField(upload_to='photos')
    is_accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.author}: {self.title}'
