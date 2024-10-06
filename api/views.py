from rest_framework import viewsets
from .models import Province, District, Ward, Place
from .serializers import ProvinceSerializer, DistrictSerializer, WardSerializer, PlaceSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return District.objects.filter(province_id=self.kwargs['province_pk'])

class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer

    def get_queryset(self):
        return Ward.objects.filter(district_id=self.kwargs['district_pk'])

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(ward_id=self.kwargs['ward_pk'])
