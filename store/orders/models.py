from django.db import models

from shop.models import ProductItem


# Create your models here.

class OrderModel(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"

    def __str__(self):
        return 'Заказ'.format(self.pk)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, related_name='items', on_delete=models.CASCADE)
    productitem = models.ForeignKey(ProductItem, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price * self.quantity
