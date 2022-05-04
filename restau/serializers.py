from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from restau.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name",)

    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)


class OwnerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Owner
        fields = ("id", "name", "type", "user")


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "name")


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ("id", "name", "district")


class WriteRestaurantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Restaurant
        fields = ("name", "owner", "rating", "district", "sector", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["owner"].queryset = Owner.objects.filter(user=user)


class ReadRestaurantSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    owner = serializers.SlugRelatedField(read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(read_only=True, slug_field='name')
    sector = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Restaurant
        fields = ("id", "name", "owner", "rating", "district", "sector", "user")
        read_only_fields = fields


class WritePictureSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Picture
        fields = ("dish", "image", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["dish"].queryset = Dish.objects.filter(user=user)


class ReadPictureSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    dish = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Picture
        fields = ("id", "dish", "image", "user")
        read_only_fields = fields


class WriteDishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dish
        fields = ("name", "cookTime", "ingredients", "price", "restaurant", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["restaurant"].queryset = Restaurant.objects.filter(user=user)


class ReadDishSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    restaurant = serializers.SlugRelatedField(read_only=True, slug_field='name')
    ingredients = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    pictures = ReadPictureSerializer(many=True)

    class Meta:
        model = Dish
        fields = ("id", "name", "cookTime", "ingredients", "pictures", "price", "restaurant", "user")
        read_only_fields = fields


class IngredientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ingredient
        fields = ("id", "name", "user")
