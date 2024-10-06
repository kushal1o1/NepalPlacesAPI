from rest_framework import serializers
from .models import Province, District, Ward, Place

class ProvinceSerializer(serializers.ModelSerializer):
    districts = serializers.StringRelatedField(many=True, read_only=True)  

    class Meta:
        model = Province
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    wards = serializers.StringRelatedField(many=True, read_only=True) 

    class Meta:
        model = District
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
