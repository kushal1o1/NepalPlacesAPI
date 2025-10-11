import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_list_districts(api_client, sample_district):
    url = reverse('district-list', kwargs={'province_name': 'Gandaki'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name']== sample_district.name

@pytest.mark.django_db
def test_minimal_districts(api_client, sample_district):
    url = reverse('district-list',kwargs={'province_name': 'Gandaki'}) + "?minimal=true"
    response = api_client.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name']== sample_district.name

