from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings


class GenderCategory(models.Model):
    CATEGORY_CHOICES = [
        ('M', 'Мужская'),
        ('F', 'Женская'),
        ('U', 'Унисекс'),
    ]
    name = models.CharField(max_length=1, choices=CATEGORY_CHOICES, unique=True, verbose_name="Категория пола")

    def __str__(self):
        return self.get_name_display()

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категории обуви')
    slug = models.SlugField(max_length=100, verbose_name='slug', unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='category_shoesimage', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Size(models.Model):
    size = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Размер')

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Brends(models.Model):
    name = models.CharField(max_length=30, verbose_name='Бренд')
    image = models.ImageField(upload_to='brend_images', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Shoes(models.Model):
    name = models.CharField(max_length=60, verbose_name='Кроссовки')
    description = models.TextField('Описание обуви')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='shoes_images', null=True, blank=True)
    #size = models.DecimalField('Размер обуви', max_digits=4, decimal_places=1, blank=True, null=True)
    color = models.CharField(max_length=20, verbose_name='Цвет', null=True, blank=True)
    gender_category = models.ForeignKey(GenderCategory, on_delete=models.CASCADE, verbose_name="Пол",  null=True, blank=True, related_name="shoes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shoes', verbose_name='Категория')
    brend = models.ForeignKey(Brends, on_delete=models.CASCADE, related_name='shoes', null=True, blank=True, verbose_name='Бренд')
    sizes = models.ManyToManyField(Size, related_name='shoes', verbose_name='Размеры', blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Обувь"
        verbose_name_plural = "Обувь"
        ordering = ['-price']
        db_table = 'custom_shoes_table'


class Rating(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('shoe', 'user')


class Review(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)  # Делает текст отзыва необязательным
    rating = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)






