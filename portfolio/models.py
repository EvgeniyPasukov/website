from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    picture = models.ImageField('Картинка', upload_to='img')
    url = models.SlugField(max_length=160, unique=True,)

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class PortfolioImages(models.Model):
    """фото к портфолио"""
    title = models.CharField("Заголовок", max_length=100, default='')
    image = models.ImageField("Изображение", upload_to="img")
    link = models.ForeignKey(Portfolio, verbose_name="портфолио", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фото к портфолио"
        verbose_name_plural = "фото к портфолио"