from django.db import models
from api.models.user import User
from api.models.product import Product
from django.contrib import admin
from rest_framework import serializers


class Order(models.Model):
    STATUSES = [
        (0, 'Новый'),
        (1, "Упаковка"),
        (2, "Отменненый"),
        (3, "Доставка"),
        (4, 'Ждет оплаты'),
        (5, 'Выполненый'),
        (6, 'Изготовление')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order_user_pk', verbose_name='Пользователь',
                             null=True)
    date_add = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    status = models.IntegerField(choices=STATUSES, default=0, verbose_name='Статус')
    product_set = models.ManyToManyField(Product, through='ProductSet')

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_basket(self):
        product_set = ProductSet.objects.all().filter(order_id=self.id)
        result = {}
        for line in product_set:
            result[line.product.id] = line.quantity
        return result



    class Meta:
        app_label = 'api'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductSet(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        app_label = 'api'


class ProductSetInline(admin.TabularInline):
    model = ProductSet
    extra = 1


class OrderInline(admin.ModelAdmin):
    inlines = (ProductSetInline,)


class BasketField(serializers.Field):

    def to_representation(self, obj):

        product_set = ProductSet.objects.all().filter(order_id=obj.get()[0].order.id)

        result = []
        for ps in product_set:
            result.append({ps.product.id: ps.quantity})
        return result

    def to_internal_value(self, data):
        return data
