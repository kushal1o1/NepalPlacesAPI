import pytest
from rest_framework.test import APIClient
from api.models import Province, District, City, Ward, Place

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_province():
    return Province.objects.create(
        name="Gandaki",
        headquarters="Pokhara",
        area=21456,
        population=2500000,
        number_of_districts=11
    )

@pytest.fixture
def sample_district(sample_province):
    return District.objects.create(
        name="Kaski",
        headquarters="Pokhara",
        area=2012,
        population=500000,
        province=sample_province
    )
@pytest.fixture
def sample_city(sample_district):
    return City.objects.create(
        name="Pokhara",
        city_type="metropolitan",
        district=sample_district
    )

@pytest.fixture
def sample_ward(sample_city):
    return Ward.objects.create(
        name="1",
        ward_no=1,
        city=sample_city
    )

@pytest.fixture
def sample_place(sample_ward):
    return Place.objects.create(
        name="Dhunge_Pani",
        place_type="Residential_areas",
        description="A village located in Pokhara Metropolitan Ward No. 1",
        ward=sample_ward ,
    )