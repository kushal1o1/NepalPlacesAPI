from django.contrib import admin
from .models import Province, District, City, Ward, Place
from import_export.admin import ImportExportModelAdmin

# Province Admin Configuration
@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'headquarters', 'area', 'population', 'number_of_districts')
    search_fields = ('name', 'headquarters')
    list_filter = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Basic Information', {'fields': ('name', 'headquarters')}),
        ('Stats', {'fields': ('area', 'population', 'number_of_districts')}),
    )

# District Admin Configuration
@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name', 'headquarters', 'area', 'population', 'province')
    search_fields = ('name', 'headquarters', 'province__name')
    list_filter = ('province', 'name')
    ordering = ('province', 'name')
    fieldsets = (
        ('District Information', {
            'fields': ('name', 'headquarters', 'area', 'population', 'province')
        }),
    )

# City Admin Configuration
@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city_type', 'district')
    search_fields = ('name', 'city_type')
    list_filter = ('city_type', 'district')
    ordering = ('name',)

# Ward Admin Configuration
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('ward_no', 'name', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    ordering = ('city', 'ward_no')
    fieldsets = (
        ('Ward Information', {
            'fields': ('ward_no', 'name', 'city')
        }),
    )

# Place Admin Configuration
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'ward')
    search_fields = ('name', 'ward__name', 'ward__city__name')
    list_filter = ('ward',)
    ordering = ('ward', 'name')
    fieldsets = (
        ('Place Information', {
            'fields': ('name', 'description', 'ward')
        }),
    )
