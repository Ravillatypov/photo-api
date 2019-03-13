from django.db import models
from django.conf import settings
from photo.managers import PhotoManager


class Country(models.Model):
    '''
    Страна, где фото было снято
    '''
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class City(models.Model):
    '''
    Город, где фото было снято
    '''
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        unique_together = (('name', 'country'),)

    def __str__(self):
        return f'{self.name} ({self.country})'


class Thing(models.Model):
    '''
    то что было снято на фото 
    '''
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.name


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
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='author')
    accepted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        null=True, 
        blank=True, 
        default=None, 
        related_name='accepted_by')
    city = models.ForeignKey(
        City, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default=None)
    things = models.ManyToManyField(Thing, blank=True, default=None)
    image = models.ImageField(upload_to='photos')
    is_accepted = models.BooleanField(default=False)

    @property
    def country(self):
        if isinstance(self.city, City):
            return self.city.country
        return None

    objects = PhotoManager()
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        unique_together = (('title', 'author'),)

    def __str__(self):
        return f'{self.author}: {self.title}'