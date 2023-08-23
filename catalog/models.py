from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
