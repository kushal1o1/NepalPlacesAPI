import pytest
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
def test_list_provinces(api_client, sample_province):
    url = reverse('province-list')  # router name: province-list
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == sample_province.name

@pytest.mark.django_db
def test_minimal_provinces(api_client, sample_province):
    url = reverse('province-list') + "?minimal=true"
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"]== sample_province.name
