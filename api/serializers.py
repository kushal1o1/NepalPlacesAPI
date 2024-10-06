from rest_framework import serializers
from .models import Province, District, Ward, Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'description']

class WardSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Ward
        fields = ['id', 'ward_no', 'name', 'places']

class DistrictSerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'headquarters', 'area', 'population', 'wards']

class ProvinceSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Province
        fields = ['id', 'name', 'headquarters', 'area', 'population', 'number_of_districts', 'districts']
