from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('Категория', max_length=150, default='name')
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField('описание', default='описание')
    image = models.ImageField('Картинка', upload_to='img', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('subcategory_list', kwargs={'category_slug': self.slug})


class SubCategory(models.Model):
    name = models.CharField('Подкатегория', max_length=150, default=True)
    description = models.TextField('Описание', default='описание')
    slug = models.SlugField(max_length=160, unique=True)
    image = models.ImageField('Картинка', upload_to='img', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list', kwargs={'category_slug': self.category.slug,
                                               'subcategory_slug': self.slug})


class Power(models.Model):
    name = models.CharField('Мощность', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мощность'
        verbose_name_plural = 'Мощность'


class Kelvin(models.Model):
    name = models.CharField('Цветовая температура, К', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.url

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
    power = models.PositiveSmallIntegerField('Мощность, Вт', default=1)
    svet_potok = models.CharField('Световой поток, Лм', max_length=20)
    temp_sveta = models.ForeignKey(Kelvin, verbose_name='Цветовая температура, К', on_delete=models.SET_NULL, null=True,)
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
    image = models.ImageField('Картинка', upload_to='img')
    description = models.TextField('Описание', blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True, db_index=True,)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'category_slug': self.subcategory.category.slug,
                                                 'subcategory_slug': self.subcategory.slug,
                                                 'product_slug': self.slug})

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
