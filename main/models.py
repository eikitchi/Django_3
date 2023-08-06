from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    ACTIV = 'Активна'
    NO_ACTIV = 'Не активна'

    SELECT_STATUS = [
        (ACTIV, 'Активна'),
        (NO_ACTIV, 'Не активна'),
    ]

    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='media', verbose_name='фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=150, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_create = models.DateTimeField(verbose_name='дата создания')
    date_change = models.DateTimeField(verbose_name='дата изменения')
    status = models.CharField(max_length=50, default=NO_ACTIV, choices=SELECT_STATUS, verbose_name='Статус')
    user = models.CharField(max_length=50, verbose_name='Создатель', **NULLABLE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Version(models.Model):
    name_of_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='наименование')
    number_of_version = models.CharField(max_length=150, verbose_name='номер версии')
    title_of_version = models.CharField(max_length=150, verbose_name='имя версии')
    actual_version = models.BooleanField(verbose_name='актуальность версии', default=True)

    def __str__(self):
        return f'{self.title_of_version} ({self.name_of_product})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
