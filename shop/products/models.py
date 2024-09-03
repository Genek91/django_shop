from django.db import models


class Category(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        blank=False,
        unique=True,
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='products/images/',
        blank=False,
    )


class Subcategory(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        blank=False,
        unique=True,
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='products/images/',
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
    )


class Product(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        blank=False,
        unique=True,
    )
    images = models.ImageField(
        verbose_name='Картинка',
        upload_to='products/images/',
        blank=False,
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        blank=False,
        max_digits=5,
        decimal_places=2,
    )
    subcategory = models.ForeignKey(
        Subcategory,
        verbose_name='Подкатегория',
        on_delete=models.CASCADE,
    )
