from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from product.models import Plant, Category, PlantImage

class PlantImageSerializer(ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ('id', 'image')


class PlantSerializer(ModelSerializer):
    images = PlantImageSerializer(many=True, read_only=True)
    discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = ('id', 'name', 'price',' final_product_price', 'discount_percentage', 'images')

    def get_discount_percentage(self, obj):
        return obj.discount_percentage()

    def final_product_price(self, obj):
        return obj.final_product_price()



class CategorySerializer(ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ('id','name', 'product_count')