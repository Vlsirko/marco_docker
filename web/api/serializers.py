from rest_framework import serializers
from api.models import Product, Category, Image, SeoBlock

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image', 'thumb')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    title_image = ImageSerializer(many=False, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'url', 'category', 'title_image', 'gallery', 'price')

