from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


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

    mead_type = models.CharField(max_length=20, choices=MeadType.choices, default=MeadType.TRADITIONAL, unique=True)

    def __str__(self):
        return self.get_mead_type_display()


class Product(models.Model):
    VOLUME_MULTIPLIERS = {
        '500ML': Decimal('1.0'),
        '1L': Decimal('1.8'),
        '4L': Decimal('5.0'),
    }

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    mead_type = models.ForeignKey('Category', on_delete=models.PROTECT)
    ingredients = ArrayField(models.CharField(max_length=254), blank=True, default=list)
    description = models.TextField()
    abv = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Base price for 500ml bottle")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_level = models.PositiveIntegerField(default=0)
    clearance = models.BooleanField(default=False)
    most_popular = models.BooleanField(default=False)

    def __str__(self):
            return self.name

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return f"{settings.STATIC_URL}images/no-product-image.png"

    @property
    def get_image_alt(self):
        if self.image or self.image_url:
            return self.name
        return f"No image available for {self.name}"

    def calculate_price_for_volume(self, volume_code):
        multiplier = self.VOLUME_MULTIPLIERS.get(volume_code, Decimal('1.0'))
        return (self.price * multiplier).quantize(Decimal('0.01'))

    @property
    def price_1l(self):
        return self.calculate_price_for_volume('1L')

    @property
    def price_4l(self):
        return self.calculate_price_for_volume('4L')

    @property
    def average_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else None
    
    @property
    def review_count(self):
        return self.reviews.count()

    def get_user_rating(self, user):
        if not user.is_authenticated:
            return None
        review = self.reviews.filter(user=user).first()
        return review.rating if review else None


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f"{self.rating} by {self.user.username} for {self.product.name}"