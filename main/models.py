from django.db import models


class Portfolio(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    picture = models.ImageField('Картинка', upload_to='img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Slider(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Описание', max_length=100)
    url = models.URLField('Ссылка', blank=True, null=True,)
    button = models.CharField('Кнопка', max_length=100, default=None, blank=True, null=True)
    picture = models.ImageField('Картинка', upload_to='img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'