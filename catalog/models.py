from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Catalog(models.Model):
    name = models.CharField('Название', max_length=50)
    vid_sv = models.CharField('Вид светильника', max_length=30)
    tip_mon = models.CharField('Тип монтажа', max_length=30)
    max_power = models.CharField('Максимальная мощность', max_length=20)
    temp_sveta = models.CharField('Температура света', max_length=20)
    svet_potok = models.CharField('Световой поток', max_length=20)
    color = models.CharField('Цвет корпуса', max_length=20)
    svet = models.CharField('Свет', max_length=50)
    srok = models.CharField('Срок службы', max_length=50)
    size = models.CharField('Габариты', max_length=100)
    napruga = models.CharField('Напряжение питания', max_length=100)
    protection = models.CharField('Степень защиты', max_length=10)
    coef_puls = models.CharField('Коэффициент пульсации', max_length=10)
    garant = models.CharField('Гарантия', max_length=10)
    image = models.ImageField('Картинка', upload_to='img', null=True, blank=True)
    url = models.SlugField(unique=True, blank=True, null=True, db_index=True,)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class CatalogImages(models.Model):
    """фото к товару"""
    title = models.CharField("Заголовок", max_length=100, default='')
    image = models.ImageField("Изображение", upload_to="img")
    link = models.ForeignKey(Catalog, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фото к товару"
        verbose_name_plural = "фото к товарам"
