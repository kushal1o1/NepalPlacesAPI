import django_filters
from .models import Place,Province,District,City,Ward
from django_filters import rest_framework as filters

class PlaceFilter(django_filters.FilterSet):
    placetype = django_filters.CharFilter(field_name='placetype', lookup_expr='iexact')  # Exact match
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # Partial match (case-insensitive)

    class Meta:
        model = Place
        fields = ['placetype', 'name']
        
class ProvinceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # Partial match (case-insensitive)
    headquarters = django_filters.CharFilter(field_name='headquarters', lookup_expr='icontains')
    min_area = filters.NumberFilter(field_name="area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="area", lookup_expr='lte')
    
    # Filter by minimum and maximum population
    min_population = filters.NumberFilter(field_name="population", lookup_expr='gte')
    max_population = filters.NumberFilter(field_name="population", lookup_expr='lte')

    # Filter by minimum and maximum number of districts
    min_districts = filters.NumberFilter(field_name="number_of_districts", lookup_expr='gte')
    max_districts = filters.NumberFilter(field_name="number_of_districts", lookup_expr='lte')

    district_name = filters.CharFilter(field_name='districts__name', lookup_expr='icontains')  # Filter provinces by district name
    district_headquarters = filters.CharFilter(field_name='districts__headquarters', lookup_expr='icontains')  # Filter by district headquarters
    min_district_area = filters.NumberFilter(field_name='districts__area', lookup_expr='gte')  # Filter districts by minimum area
    max_district_area = filters.NumberFilter(field_name='districts__area', lookup_expr='lte')  # Filter districts by maximum area
    min_district_population = filters.NumberFilter(field_name='districts__population', lookup_expr='gte')  # Filter districts by minimum population
    max_district_population = filters.NumberFilter(field_name='districts__population', lookup_expr='lte')  # Filter districts by maximum population
    
      # Filters for related City fields
    city_name = filters.CharFilter(field_name='districts__cities__name', lookup_expr='icontains')  # Filter provinces by city name
   


    # Filters for related Place fields
    place_name = filters.CharFilter(field_name='districts__cities__wards__places__name', lookup_expr='icontains')  # Filter provinces by place name
   
    class Meta:
        model = Province
        fields = ['headquarters','name','min_area', 'max_area','min_population', 'max_population','min_districts', 'max_districts', 'district_name','district_headquarters','min_district_area','max_district_area','min_district_population','max_district_population','city_name',
            'place_name',

        ]
        
        
class DistrictFilter(filters.FilterSet):
    # Filter by minimum and maximum area
    min_area = filters.NumberFilter(field_name="area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="area", lookup_expr='lte')
    
    # Filter by minimum and maximum population
    min_population = filters.NumberFilter(field_name="population", lookup_expr='gte')
    max_population = filters.NumberFilter(field_name="population", lookup_expr='lte')
    
    # Filter by province name
    province_name = filters.CharFilter(field_name='province__name', lookup_expr='iexact')

    class Meta:
        model = District
        fields = ['min_area', 'max_area', 'min_population', 'max_population', 'province_name']
        
class CityFilter(filters.FilterSet):
    # Filter by district name
    district_name = filters.CharFilter(field_name='district__name', lookup_expr='iexact')
    
    # Filter by city type
    city_type = filters.ChoiceFilter(field_name='city_type', choices=City._meta.get_field('city_type').choices)

    class Meta:
        model = City
        fields = ['district_name', 'city_type']
        
class WardFilter(filters.FilterSet):
    # Filter by city name
    city_name = filters.CharFilter(field_name='city__name', lookup_expr='iexact')

    # Filter by ward number
    ward_no = filters.NumberFilter(field_name='ward_no')

    class Meta:
        model = Ward
        fields = ['city_name', 'ward_no']
