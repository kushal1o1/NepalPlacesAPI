from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Province, District, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, WardSerializer, PlaceSerializer
from rest_framework.permissions import AllowAny

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return District.objects.filter(province_id=self.kwargs['province_pk'])

    def perform_create(self, serializer):
        province = Province.objects.get(pk=self.kwargs['province_pk'])
        serializer.save(province=province)

class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer

    def get_queryset(self):
        return Ward.objects.filter(district_id=self.kwargs['district_pk'])

    def perform_create(self, serializer):
        district = District.objects.get(pk=self.kwargs['district_pk'])
        serializer.save(district=district)
        permission_classes = [AllowAny]

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(ward_id=self.kwargs['ward_pk'])

    def perform_create(self, serializer):
        ward = Ward.objects.get(pk=self.kwargs['ward_pk'])
        serializer.save(ward=ward)
