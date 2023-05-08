from django.contrib import admin

# Register your models here.

from .models import OrderModel, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['productitem']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'email',
                    'address', 'city', 'created_at']
    list_filter = ['created_at']
    inlines = [OrderItemInline]


admin.site.register(OrderModel, OrderAdmin)
