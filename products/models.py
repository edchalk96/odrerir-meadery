from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    class MeadType(models.TextChoices):
        TRADITIONAL = 'TRADITIONAL', 'Traditional'
        MELOMEL = 'MELOMEL', 'Melomel (Fruit)'
        METHEGLIN = 'METHEGLIN', 'Metheglin (Spiced)'
        CYSER = 'CYSER', 'Cyser (Apple)'
        PYMENT = 'PYMENT', 'Pyment (Grape)'
        BRAGGOT = 'BRAGGOT', 'Braggot (Malt/Ale)'
        CAPSICUMEL = 'CAPSICUMEL', 'Capsicumel (Chilli/Pepper)'
        HYDROMEL = 'HYDROMEL', 'Hydromel (Session/Low-ABV)'
        ACERGLYN = 'ACERGLYN', 'Acerglyn (Maple)'
        ACCESSORIES = 'ACCESSORIES', 'Accessories & Merch'

    mead_type = models.CharField(max_length=20, choices=MeadType.choices, default=MeadType.TRADITIONAL,)

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.get_mead_type_display()})"


class Product(models.Model):
    class VolumeOptions(models.TextChoices):
        VOLUME_500 = '500ML', '500ml'
        VOLUME_1 = '1L', '1L'
        VOLUME_4 = '4L', '4L'

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    mead_type = models.ForeignKey('Category', on_delete=models.PROTECT)
    ingredients = ArrayField(models.CharField(max_length=254), blank=True, default=list)
    description = models.TextField()
    abv = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    volume = models.CharField(max_length=10, choices=VolumeOptions.choices, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_level = models.PositiveIntegerField(default=0)
    clearance = models.BooleanField(default=False)
    most_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name