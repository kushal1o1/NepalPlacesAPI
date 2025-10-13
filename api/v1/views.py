from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import Province, District, City, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, CitySerializer, WardSerializer, PlaceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import PlaceFilter ,ProvinceFilter,DistrictFilter,CityFilter,WardFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from rest_framework.response import Response
from django_ratelimit.decorators import ratelimit
from rest_framework import status
from ..services import MinimalResponseMixin , error_response

class ProvinceViewSet(MinimalResponseMixin,viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'name'  # Use 'name' instead of 'id'
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProvinceFilter
    search_fields = ['name', 'headquarters', 'districts__name', 'districts__cities__name', 'districts__cities__wards__name', 'districts__cities__wards__places__name']
    ordering_fields = ['name', 'population', 'area','headquarters','districts__name']
    

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @method_decorator(ratelimit(key='ip', rate='5/m', method='GET', block=False))
    def list(self, request, *args, **kwargs):
        if request.limited:
            return error_response(
                code='RATE_LIMIT_EXCEEDED',
                message='Rate limit exceeded. Please retry in a minute.', http_status=status.HTTP_429_TOO_MANY_REQUESTS)
        return super().list(request, *args, **kwargs)

class DistrictViewSet(MinimalResponseMixin,viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = DistrictFilter
    search_fields = ['name','headquarters','area','population']
    ordering_fields = ['name', 'population', 'area','headquarters']

    def get_queryset(self):
        province_name = self.request.query_params.get('province', None)
        if province_name:
            return District.objects.filter(province__name=province_name)
        return District.objects.all()  # For flat access

class CityViewSet(MinimalResponseMixin,viewsets.ModelViewSet):
    serializer_class = CitySerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = CityFilter
    search_fields = ['name','city_type',"wards__ward_no","wards__name"]
    ordering_fields = ['name', 'city_type', 'wards__ward_no','wards__name']
    

    def get_queryset(self):
        district_name = self.kwargs.get('district_name', None)
        if district_name:
            return City.objects.filter(district__name=district_name)
        return City.objects.all()  # For flat access


class WardViewSet(MinimalResponseMixin,viewsets.ModelViewSet):
    serializer_class = WardSerializer
    lookup_field = 'name'  # Use 'name' as primary key
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = WardFilter
    search_fields = ['ward_no','name','places__name',"places__place_type"]
    ordering_fields = ['ward_no','name','places__name',"places__place_type"]
    
    

    def get_queryset(self):
        city_name = self.request.query_params.get('city_name', None)
        if city_name:
            return Ward.objects.filter(city_name=city_name)
        return Ward.objects.all()  # For flat access

class PlaceViewSet(MinimalResponseMixin, viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    lookup_field = 'name'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PlaceFilter
    search_fields = ['name', 'description', 'place_type']
    ordering_fields = ['name', 'place_type']

    def get_queryset(self):
        ward_name = self.kwargs.get('ward_name', None)
        if ward_name:
            return Place.objects.filter(ward__name=ward_name)
        return Place.objects.all()

    def list(self, request, *args, **kwargs):
        ward_name = self.kwargs.get('ward_name')
        cache_key = f'places_{ward_name}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            response = Response({
                'count': len(serializer.data),
                'next': None,
                'previous': None,
                'results': serializer.data
            })

        # ✅ Cache entire paginated response for 10 minutes
        cache.set(cache_key, response.data, 60 * 10)
        return response

    # Invalidate cache on changes
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete(f'places_{self.kwargs.get("ward_name")}')
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete(f'places_{self.kwargs.get("ward_name")}')
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete(f'places_{self.kwargs.get("ward_name")}')
        return response
