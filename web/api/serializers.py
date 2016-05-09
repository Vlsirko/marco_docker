from rest_framework import serializers
from api.models.product import Product
from api.models.category import Category
from api.models.banners import Slider
from api.models.sale import Sale
from api.models.images import Image

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
        fields = ('title',
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
