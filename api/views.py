from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Province, District, City, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, CitySerializer, WardSerializer, PlaceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PlaceFilter ,ProvinceFilter,DistrictFilter,CityFilter,WardFilter
from rest_framework.filters import SearchFilter


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'name'  # Use 'name' instead of 'id'
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = ProvinceFilter
    search_fields = ['name', 'headquarters', 'districts__name', 'districts__cities__name', 'districts__cities__wards__name', 'districts__cities__wards__places__name']

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = DistrictFilter
    search_fields = ['name','headquarters','area','population']

    def get_queryset(self):
        province_name = self.request.query_params.get('province', None)
        if province_name:
            return District.objects.filter(province__name=province_name)
        return District.objects.all()  # For flat access

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = CityFilter
    search_fields = ['name','city_type',"wards__ward_no","wards__name"]

    def get_queryset(self):
        district_name = self.request.query_params.get('district_name', None)
        if district_name:
            return City.objects.filter(district__name=district_name)
        return City.objects.all()  # For flat access


class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = WardFilter
    search_fields = ['ward_no','name','places__name',"places__place_type"]
    

    def get_queryset(self):
        city_name = self.request.query_params.get('city_name', None)
        if city_name:
            return Ward.objects.filter(city_name=city_name)
        return Ward.objects.all()  # For flat access

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = PlaceFilter
    search_fields = ['name','description','place_type']
    

    def get_queryset(self):
        ward_name = self.request.query_params.get('ward_name', None)
        if ward_name:
            return Place.objects.filter(ward_name=ward_name)
        return Place.objects.all()  # For flat access
       