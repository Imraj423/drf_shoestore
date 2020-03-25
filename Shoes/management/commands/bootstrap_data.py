
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
        ShoeColor.objects.create(color='red')
        ShoeColor.objects.create(color='orange')
        ShoeColor.objects.create(color='yellow')
        ShoeColor.objects.create(color='green')
        ShoeColor.objects.create(color='blue')
        ShoeColor.objects.create(color='indigo')
        ShoeColor.objects.create(color='violet')
        ShoeColor.objects.create(color='white')
        ShoeColor.objects.create(color='black')
