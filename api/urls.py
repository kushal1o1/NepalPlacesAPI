from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProvinceViewSet, DistrictViewSet, CityViewSet, WardViewSet, PlaceViewSet

router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet, basename='province')
router.register(r'provinces/(?P<province_name>[^/.]+)/districts', DistrictViewSet, basename='district')
router.register(r'provinces/(?P<province_name>[^/.]+)/districts/(?P<district_name>[^/.]+)/cities', CityViewSet, basename='city')
router.register(r'provinces/(?P<province_name>[^/.]+)/districts/(?P<district_name>[^/.]+)/cities/(?P<city_name>[^/.]+)/wards', WardViewSet, basename='ward')
router.register(r'provinces/(?P<province_name>[^/.]+)/districts/(?P<district_name>[^/.]+)/cities/(?P<city_name>[^/.]+)/wards/(?P<ward_name>[^/.]+)/places', PlaceViewSet, basename='place')

router.register(r'districts', DistrictViewSet, basename='district_flat')
router.register(r'cities', CityViewSet, basename='city_flat')
router.register(r'wards', WardViewSet, basename='ward_flat')
router.register(r'places', PlaceViewSet, basename='place_flat')

urlpatterns = [
    path('api/', include(router.urls)),
]
