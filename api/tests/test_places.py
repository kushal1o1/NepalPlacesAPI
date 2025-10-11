import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_list_places(api_client, sample_place):
    url = reverse('place-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski','city_name':'Pokhara','ward_name':'1'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"] == sample_place.name

@pytest.mark.django_db
def test_minimal_places(api_client, sample_place):
    url = reverse('place-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski','city_name':'Pokhara','ward_name':'1'}) + "?minimal=true"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"] == sample_place.name

@pytest.mark.django_db
def test_search_places(api_client, sample_place):
    url = reverse('place-list',kwargs={'province_name': 'Gandaki','district_name':'Kaski','city_name':'Pokhara','ward_name':'1'}) + f"?search={sample_place.name}"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]["name"] == sample_place.name
