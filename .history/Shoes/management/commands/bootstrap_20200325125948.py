
from django.core.management.base import BaseCommand
from Shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'Show ShoeType and ShoeColor'

    def handle(self, *args, **options):
        ShoeType.objects.create(style='sneaker')
        ShoeType.objects.create(style='boot')
        ShoeType.objects.create(style='sandal')
        ShoeType.objects.create(style='dress')
        ShoeType.objects.create(style='other')
        ShoeColor.objects.create(color_name='red')
        ShoeColor.objects.create(color_name='orange')
        ShoeColor.objects.create(color_name='yellow')
        ShoeColor.objects.create(color_name='green')
        ShoeColor.objects.create(color_name='blue')
        ShoeColor.objects.create(color_name='indigo')
        ShoeColor.objects.create(color_name='violet')
        ShoeColor.objects.create(color_name='white')
        ShoeColor.objects.create(color_name='black')
