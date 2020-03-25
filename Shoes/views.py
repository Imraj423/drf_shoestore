from rest_framework import viewsets
from Shoes.models import Manufacturer, ShoeColor, ShoeType, Shoe
from Shoes.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer

# Create your views here.


class ManufacturerViewSet(viewsets.ViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ShoeColorViewSet(viewsets.ViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(viewsets.ViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()


class ShoeViewSet(viewsets.ViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()
