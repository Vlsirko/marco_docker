from rest_framework import serializers
from api.models.product import Product
from api.models.category import Category
from api.models.banners import Slider
from api.models.sale import Sale
from api.models.images import Image
from api.models.order import Order, ProductSet, BasketField
from api.models.user import User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'path')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'url')


class SaleSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = ('title', 'description', 'image')


class SliderSerializer(serializers.ModelSerializer):
    gallery = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Slider
        fields = ('gallery',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    sales = SaleSerializer(many=True, read_only=True)
    title_image = ImageSerializer(many=False, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)
    lookup_field = 'url'

    class Meta:
        model = Product
        fields = ('id',
                  'title',
                  'category',
                  'title_image',
                  'gallery',
                  'price',
                  'description',
                  'url',
                  'is_new',
                  'is_sale',
                  'is_preorder',
                  'sales')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class OrderSerializer(serializers.ModelSerializer):
    basket = serializers.DictField(source='get_basket')

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'basket')

    def create(self, validated_data):
        if 'get_basket' not in validated_data:
            raise serializers.ValidationError('Can\'t create empty order')

        basket = validated_data.pop('get_basket')
        order = Order.objects.create(**validated_data)
        for product_id in basket:
            product = Product.objects.get(pk=product_id)
            if product:
                ProductSet.objects.create(order=order, product=product, quantity=basket[product_id])
        return order


