from django.contrib import admin
from django.db import models
from django.db.models import Sum
from api.models.product import Product
from api.models.user import User
from django.core import urlresolvers
from django.utils.html import format_html


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

    DELIVERY_METHODS = [
        (0, 'Самовывоз'),
        (1, 'Новая Почта'),
        (2, 'Укрпочта')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order_user_pk', verbose_name='Пользователь',
                             null=True)
    date_add = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    status = models.IntegerField(choices=STATUSES, default=0, verbose_name='Статус')
    delivery_method = models.IntegerField(choices=DELIVERY_METHODS, default=0, verbose_name='Способ доставки')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий к заказу')
    comment_admin = models.TextField(null=True, blank=True, verbose_name='Комментарий продавца')
    product_set = models.ManyToManyField(Product, through='ProductSet')

    @property
    def total_amount(self):
        """
        Возвращает сумму заказа
        """
        return self.product_set.aggregate(Sum('price')).get('price__sum')

    @property
    def basket(self):
        """
        Возвращает содержимое корзины в виде словаря где ключем есть id товара, а значением его количество
        """
        product_set = ProductSet.objects.all().filter(order_id=self.id)
        result = {}
        for line in product_set:
            result[line.product.id] = line.quantity
        return result

    @property
    def basket_for_admin(self):
        """
        Возвращает html для представления корзины в админке
        """
        basket = self.basket
        products = self.product_set.all()
        html = '<ul>'
        pattern = '<li>{src}<a href="{href}">{title}</a> x {count}</li>'
        for product in products:
            html += pattern.format(**{
                'src': product.title_image_thumb,
                'href': urlresolvers.reverse('admin:api_product_change', args=(product.id, ), current_app='api'),
                'title': product.title,
                'count': basket.get(product.id)
            })
        html += '</ul>'
        return format_html(html)

    @property
    def user_info(self):
        user = self.user
        return format_html('<br> '.join((user.name, user.email, user.phone)))

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

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
    extra = 0