from django.db import models


class Portfolio(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    picture = models.ImageField('Картинка', upload_to='img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Production(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    picture = models.ImageField('Картинка', upload_to='img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'