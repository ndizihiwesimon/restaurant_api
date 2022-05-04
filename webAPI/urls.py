from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from restau import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, basename='user'),
router.register(r'owners', views.OwnerViewSet, basename='owner'),
router.register(r'districts', views.DistrictViewSet, basename='district'),
router.register(r'sectors', views.SectorViewSet, basename='sector'),
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant'),
router.register(r'ingredients', views.IngredientViewSet, basename='ingredient'),
router.register(r'pictures', views.PictureViewSet, basename='picture'),
router.register(r'dishes', views.DishViewSet, basename='dish'),


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token, name="obtain-auth-token")
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
