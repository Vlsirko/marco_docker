from rest_framework import serializers
from api.models.product import Product
from api.models.category import Category
from api.models.banners import Slider
from api.models.sale import Sale
from api.models.images import Image
from api.models.order import Order, ProductSet
from api.models.user import User
from api.models.seo_block import SeoBlock


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'path')


class SeoBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoBlock
        exclude = ('object_id', 'content_type', 'id')


class CategorySerializer(serializers.ModelSerializer):
    seo_block = SeoBlockSerializer(many=False)

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'url', 'seo_block')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('title', 'description', 'thumb')


class SliderSerializer(serializers.ModelSerializer):
    gallery = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Slider
        fields = ('gallery',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    sales = SaleSerializer(many=True, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)
    seo_block = SeoBlockSerializer(many=False)
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
                  'sales',
                  'seo_block')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone')
        extra_kwargs = {
            'email': {
                'validators': []
            }
        }


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer для заказа
    """
    basket = serializers.DictField(required=True)
    user = UserSerializer(required=True, partial=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'basket', 'total_amount', 'comment', 'delivery_method', 'comment_admin')
        read_only_fields = ('comment_admin',)

    def create(self, validated_data):
        basket = validated_data.pop('basket')
        user_data = validated_data.pop('user')
        user_email = user_data.pop('email')
        validated_data['user'] = User.objects.get_or_create(email=user_email, defaults=user_data)[0]

        order = Order.objects.create(**validated_data)
        for product_id in basket:
            product = Product.objects.get(pk=product_id)
            if product:
                ProductSet.objects.create(order=order, product=product, quantity=basket[product_id])

        return order

