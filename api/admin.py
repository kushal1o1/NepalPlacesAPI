from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Province, District, City, Ward, Place

# Resources
class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province
        fields = ('name', 'headquarters', 'area', 'population', 'number_of_districts')  # Use 'name' instead of 'id'
        import_id_fields = ['name']  # Make sure 'name' is used as the key field

class DistrictResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Convert 'province' field to its primary key (name) during import
        try:
            province = Province.objects.get(name=row['province'])
            row['province'] = province.pk
        except Province.DoesNotExist:
            row['province'] = None  # or handle the error if province not found
        return super().before_import_row(row, **kwargs)

    class Meta:
        model = District
        fields = ('name', 'province', 'headquarters', 'area', 'population')
        import_id_fields = ['name']

class CityResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Convert 'district' field to its primary key (name) during import
        try:
            district = District.objects.get(name=row['district'])
            row['district'] = district.pk
        except District.DoesNotExist:
            row['district'] = None  # or handle the error if district not found
        return super().before_import_row(row, **kwargs)

    class Meta:
        model = City
        fields = ('name', 'district', 'city_type')
        import_id_fields = ['name']

class WardResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Convert 'city' field to its primary key (name) during import
        try:
            city = City.objects.get(name=row['city'])
            row['city'] = city.pk
        except City.DoesNotExist:
            row['city'] = None  # or handle the error if city not found
        return super().before_import_row(row, **kwargs)

    class Meta:
        model = Ward
        fields = ('name', 'city', 'ward_no')
        import_id_fields = ['name']

class PlaceResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Convert 'ward' field to its primary key (name) during import
        try:
            ward = Ward.objects.get(name=row['ward'])
            row['ward'] = ward.pk
        except Ward.DoesNotExist:
            row['ward'] = None  # or handle the error if ward not found
        return super().before_import_row(row, **kwargs)

    class Meta:
        model = Place
        fields = ('name', 'ward', 'description')
        import_id_fields = ['name']

# Admin Classes
@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    resource_class = ProvinceResource
    list_display = ('name', 'headquarters', 'area', 'population', 'number_of_districts')

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictResource
    list_display = ('name', 'province', 'headquarters', 'area', 'population')

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = ('name', 'district', 'city_type')

@admin.register(Ward)
class WardAdmin(ImportExportModelAdmin):
    resource_class = WardResource
    list_display = ('name', 'city', 'ward_no')

@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    resource_class = PlaceResource
    list_display = ('name', 'ward', 'description')
