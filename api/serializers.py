from rest_framework import serializers
from .models import Province, District, City, Ward, Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name','place_type', 'description']

class WardSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Ward
        fields = ['name', 'ward_no', 'places']

class CitySerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['name', 'city_type', 'wards']

class DistrictSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['name', 'headquarters', 'area', 'population', 'cities']

class ProvinceSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Province
        fields = ['name', 'headquarters', 'area', 'population', 'number_of_districts', 'districts']
