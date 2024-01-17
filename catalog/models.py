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


class Power(models.Model):
    name = models.CharField('Мощность', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мощность'
        verbose_name_plural = 'Мощность'


class Kelvin(models.Model):
    name = models.PositiveSmallIntegerField('Цветовая температура, К', default=0)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цветовая температура'
        verbose_name_plural = 'Цветовые температуры'


class Protection(models.Model):
    name = models.CharField('Степень защиты', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Степень защиты'
        verbose_name_plural = 'Степени защиты'


class Catalog(models.Model):
    name = models.CharField('Название', max_length=50)
    lamp_type = models.CharField('Тип ламп', max_length=50, default='')
    rass_type = models.CharField('Тип рассеивателя', max_length=30, default='')
    max_power = models.ForeignKey(Power, verbose_name='Мощность, Вт', on_delete=models.SET_NULL, null=True)
    svet_potok = models.CharField('Световой поток, Лм', max_length=20)
    temp_sveta = models.PositiveSmallIntegerField('Цветовая температура, К', default=0)
    napruga = models.CharField('Номинальное напряжение, В', max_length=100)
    herz = models.CharField('Номинальная частота, Гц', max_length=100, default='')
    koef_power = models.CharField('Коэффициент мощности', max_length=100, default='')
    koef_ra = models.CharField('Коэффициент цветопередачи, Ra', max_length=100, default='')
    protection = models.ForeignKey(Protection, verbose_name='Степень защиты', on_delete=models.SET_NULL, null=True,)
    coef_puls = models.CharField('Коэффициент пульсации, %', max_length=10)
    usage_temp = models.CharField('Допустимая температура эксплуатации, С', max_length=20, default='')
    size = models.CharField('Габариты', max_length=100)
    tip_mon = models.CharField('Тип монтажа', max_length=30)
    garant = models.CharField('Гарантия', max_length=10)
    image = models.ImageField('Картинка', upload_to='img', null=True, blank=True)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True,)
    url = models.SlugField(unique=True, blank=True, null=True, db_index=True,)

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
