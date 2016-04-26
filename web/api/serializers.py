from rest_framework import serializers
from api.models.product import Product
from api.models.category import Category
from api.models.images import ProductImage, SliderImage
from api.models.banners import Slider


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'url')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'thumb')


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ('image', 'link', 'title')


class SliderSerializer(serializers.ModelSerializer):
    gallery = SliderImageSerializer(many=True, read_only=True)

    class Meta:
        model = Slider
        fields = ('gallery',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    title_image = ImageSerializer(many=False, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'title_image', 'gallery', 'price')
