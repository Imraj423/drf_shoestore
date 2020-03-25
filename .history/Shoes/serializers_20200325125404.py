from rest_framework import serializers

from Shoes.models import Manufacturer, ShoeColor, ShoeType, Shoe


class Manufacturer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website'
        ]


class ShoeColor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color'
        ]


class ShoeType_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'style'
        ]


class Shoe_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'material',
            'fasten_type',
            'manufacturer',
            'color',
            'shoe_type'
        ]
