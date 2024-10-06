from rest_framework_nested import routers
from django.urls import path, include
from .views import ProvinceViewSet, DistrictViewSet, WardViewSet, PlaceViewSet

# Root router
router = routers.SimpleRouter()
router.register(r'provinces', ProvinceViewSet)

# Nested router for districts under a province
district_router = routers.NestedSimpleRouter(router, r'provinces', lookup='province')
district_router.register(r'districts', DistrictViewSet, basename='province-districts')

# Nested router for wards under a district
ward_router = routers.NestedSimpleRouter(district_router, r'districts', lookup='district')
ward_router.register(r'wards', WardViewSet, basename='district-wards')

# Nested router for places under a ward
place_router = routers.NestedSimpleRouter(ward_router, r'wards', lookup='ward')
place_router.register(r'places', PlaceViewSet, basename='ward-places')

# Include all the routers in urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(district_router.urls)),
    path('api/', include(ward_router.urls)),
    path('api/', include(place_router.urls)),
]
