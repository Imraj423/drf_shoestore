from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color = models.CharField(
        max_length=10,
        )

    def __str__(self):
        return self.color
# 

class Shoe(models.Model):
    size = models.IntegerField()
    material = models.CharField(max_length=50)
    fasten_type = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        ShoeColor, on_delete=models.CASCADE
    )
    shoe_type = models.ForeignKey(
        ShoeType, on_delete=models.CASCADE
    )
