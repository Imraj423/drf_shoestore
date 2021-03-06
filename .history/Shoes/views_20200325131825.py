from rest_framework import viewsets
from Shoes.models import Manufacturer, ShoeColor, ShoeType, Shoe
from Shoes.serializers import Manufacturer_Serializer, ShoeColor_Serializer, ShoeType_Serializer, Shoe_Serializer

# Create your views here.


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = Manufacturer_Serializer
    queryset = Manufacturer.objects.all()


class ShoeColorViewSet(viewsets.ModelViewSet):
    serializer_class = ShoeColor_Serializer
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ShoeType_Serializer
    queryset = ShoeType.objects.all()


class ShoeViewSet(viewsets.ModelViewSet):
    serializer_class = Shoe_Serializer
    queryset = Shoe.objects.all()
