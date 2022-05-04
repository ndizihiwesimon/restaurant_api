from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Owner(models.Model):
    class OwnerType(models.TextChoices):
        INDIVIDUAL = 'Individual'
        COMPANY = 'Company'

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=OwnerType.choices, default=OwnerType.INDIVIDUAL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=30, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.district.name} - {self.name}"


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, related_name="restaurants")
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0),
                                 ], )
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")

    def __str__(self):
        return f"{self.owner.name} - {self.name} - {self.rating} Stars"


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    cookTime = models.DurationField()
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="dishes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dishes")

    def __str__(self):
        return self.name


class Picture(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='dishes/', default='dishes/blank.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pictures")


