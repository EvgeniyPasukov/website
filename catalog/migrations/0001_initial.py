# Generated by Django 4.2.11 on 2024-03-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('lamp_type', models.CharField(default='', max_length=50, verbose_name='Тип ламп')),
                ('rass_type', models.CharField(default='', max_length=30, verbose_name='Тип рассеивателя')),
                ('power', models.PositiveSmallIntegerField(default=1, verbose_name='Мощность, Вт')),
                ('svet_potok', models.CharField(max_length=20, verbose_name='Световой поток, Лм')),
                ('napruga', models.CharField(max_length=100, verbose_name='Номинальное напряжение, В')),
                ('herz', models.CharField(default='', max_length=100, verbose_name='Номинальная частота, Гц')),
                ('koef_power', models.CharField(default='', max_length=100, verbose_name='Коэффициент мощности')),
                ('koef_ra', models.CharField(default='', max_length=100, verbose_name='Коэффициент цветопередачи, Ra')),
                ('coef_puls', models.CharField(max_length=10, verbose_name='Коэффициент пульсации, %')),
                ('usage_temp', models.CharField(default='', max_length=20, verbose_name='Допустимая температура эксплуатации, С')),
                ('size', models.CharField(max_length=100, verbose_name='Габариты')),
                ('tip_mon', models.CharField(max_length=30, verbose_name='Тип монтажа')),
                ('garant', models.CharField(max_length=10, verbose_name='Гарантия')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('url', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Kelvin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Цветовая температура, К')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Цветовая температура',
                'verbose_name_plural': 'Цветовые температуры',
            },
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Мощность')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Мощность',
                'verbose_name_plural': 'Мощность',
            },
        ),
        migrations.CreateModel(
            name='Protection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Степень защиты')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Степень защиты',
                'verbose_name_plural': 'Степени защиты',
            },
        ),
        migrations.CreateModel(
            name='CatalogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='img', verbose_name='Изображение')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalog', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'фото к товару',
                'verbose_name_plural': 'фото к товарам',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='protection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.protection', verbose_name='Степень защиты'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='temp_sveta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.kelvin', verbose_name='Цветовая температура, К'),
        ),
    ]