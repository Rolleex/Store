from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title


class ProductItem(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(decimal_places=0, max_digits=9)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/images/%Y/%m/%d/')
    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.title
