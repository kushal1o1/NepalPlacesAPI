from rest_framework import viewsets
from .models import Province, District, City, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, CitySerializer, WardSerializer, PlaceSerializer
from rest_framework.permissions import AllowAny

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [AllowAny]

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return District.objects.filter(province_id=self.kwargs['province_pk'])

    def perform_create(self, serializer):
        province = Province.objects.get(pk=self.kwargs['province_pk'])
        serializer.save(province=province)

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return City.objects.filter(district_id=self.kwargs['district_pk'])

    def perform_create(self, serializer):
        district = District.objects.get(pk=self.kwargs['district_pk'])
        serializer.save(district=district)

class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Ward.objects.filter(city_id=self.kwargs['city_pk'])

    def perform_create(self, serializer):
        city = City.objects.get(pk=self.kwargs['city_pk'])
        serializer.save(city=city)

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Place.objects.filter(ward_id=self.kwargs['ward_pk'])

    def perform_create(self, serializer):
        ward = Ward.objects.get(pk=self.kwargs['ward_pk'])
        serializer.save(ward=ward)
