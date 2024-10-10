from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Province, District, City, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, CitySerializer, WardSerializer, PlaceSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'name'  # Use 'name' instead of 'id'

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    lookup_field = 'name'  # Use 'name' as primary key

    def get_queryset(self):
        province_name = self.kwargs['province_name']
        return District.objects.filter(province__name=province_name)

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    lookup_field = 'name'  # Use 'name' as primary key

    def get_queryset(self):
        district_name = self.kwargs['district_name']
        return City.objects.filter(district__name=district_name)

class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    lookup_field = 'name'  # Use 'name' as primary key

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        return Ward.objects.filter(city__name=city_name)

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    lookup_field = 'name'  # Use 'name' as primary key

    def get_queryset(self):
        ward_name = self.kwargs['ward_name']
        return Place.objects.filter(ward__name=ward_name)
