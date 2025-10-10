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
