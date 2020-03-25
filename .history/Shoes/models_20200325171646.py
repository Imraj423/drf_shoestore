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


# Joe grew up in the African Savanna, when he was a wee toddler, he wandered away from his family while they were on safari. He was found by a pack of hyenas and instead of being eaten they took him in as their own, he lived as part of the pack for 10 years. Hunting and scavenging and loving life, eventually though, he started to realize he was different and wanted to know why. One night he wandered away as the pack was asleep and made his way towards a light in the horizon. After what seemed like days, he came to a settlement of animals that looked just like him, but they weren't animals, they were people. He approached the settlement and was met by two men who were surprised by his rough appearance. It took them a while to get rabid Joe to calm down and go with them, he was like a wild animal, couldn’t speak, walk upright, stank to high hell, but after a much needed cleaning and extensive rehab, he was reunited with his family and able to rejoin society. Joe was naturally gifted and blew through his schooling and is now teaching Django at Kenzie Academy.
