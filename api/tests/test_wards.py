import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_list_wards(api_client, sample_ward):
    url = reverse('ward-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski','city_name':'Pokhara'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"] == sample_ward.name

@pytest.mark.django_db
def test_minimal_wards(api_client, sample_ward):
    url = reverse('ward-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski','city_name':'Pokhara'}) + "?minimal=true"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"] == sample_ward.name
