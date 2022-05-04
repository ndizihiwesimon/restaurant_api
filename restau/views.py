from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from restau.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OwnerSerializer

    def get_queryset(self):
        return Owner.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        resto = Restaurant.objects.filter(owner=pk)
        serializer = ReadRestaurantSerializer(resto, many=True)
        return Response(serializer.data)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        resto = Restaurant.objects.filter(district=pk)
        serializer = ReadRestaurantSerializer(resto, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def sectors(self, request, pk=None):
        sectors = Sector.objects.filter(district=pk)
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        resto = Restaurant.objects.filter(sector=pk)
        serializer = ReadRestaurantSerializer(resto, many=True)
        return Response(serializer.data)


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', ]

    def get_queryset(self):
        return Restaurant.objects.select_related("owner", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadRestaurantSerializer
        return WriteRestaurantSerializer

    @action(detail=True, methods=['get'])
    def dishes(self, request, pk=None):
        context = Dish.objects.filter(restaurant=pk)
        serializer = ReadDishSerializer(context, many=True)
        return Response(serializer.data)


class DishViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Dish.objects.select_related("restaurant", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadDishSerializer
        return WriteDishSerializer


class PictureViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Picture.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadPictureSerializer
        return WritePictureSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.filter(user=self.request.user)
