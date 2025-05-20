from django.db import models
from slugify import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
        # return reverse('shop:category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True,verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ['category', 'name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        slug_name = slugify(self.name)
        slug = f'{slug_name}-{self.pk}'
        self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
        # return reverse('shop:product_detail', kwargs={'slug': self.slug})