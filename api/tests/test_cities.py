import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_list_cities(api_client, sample_city):
    url = reverse('city-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == sample_city.name

@pytest.mark.django_db
def test_minimal_cities(api_client, sample_city):
    url = reverse('city-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski'}) + "?minimal=true"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == sample_city.name
