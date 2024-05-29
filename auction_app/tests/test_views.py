# auction_app/tests/test_views.py


import os
from django.conf import settings

# Configurar las variables de entorno necesarias
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

# Configurar la configuración de Django
settings.configure()

import json
from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from auction_app.models import Auction, Artwork, Customer, Bid, Admin

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return mixer.blend(User)

# Tests for AuctionViewSet
@pytest.mark.django_db
def test_auction_list(api_client, user):
    url = reverse('auction_app:auction-list')
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_auction_create(api_client, user):
    url = reverse('auction_app:auction-list')
    data = {
        'auction_name': 'Test Auction',
        'auction_description': 'This is a test auction',
        'start_date': '2024-06-01T00:00:00Z',
        'end_date': '2024-06-10T00:00:00Z',
        'status': 'active'
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201

    # Verify the created auction
    assert Auction.objects.filter(auction_name='Test Auction').exists()

@pytest.mark.django_db
def test_auction_retrieve(api_client, user):
    auction = mixer.blend(Auction)
    url = reverse('auction_app:auction-detail', kwargs={'pk': auction.pk})
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_auction_update(api_client, user):
    auction = mixer.blend(Auction)
    url = reverse('auction_app:auction-detail', kwargs={'pk': auction.pk})
    data = {
        'auction_name': 'Updated Name',
        'status': 'inactive'
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    auction.refresh_from_db()
    assert auction.auction_name == 'Updated Name'
    assert auction.status == 'inactive'

@pytest.mark.django_db
def test_auction_delete(api_client, user):
    auction = mixer.blend(Auction)
    url = reverse('auction_app:auction-detail', kwargs={'pk': auction.pk})
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Auction.objects.filter(pk=auction.pk).exists()

# Tests for ArtworkViewSet
@pytest.mark.django_db
def test_artwork_list(api_client, user):
    url = reverse('auction_app:artwork-list')
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_artwork_create(api_client, user):
    url = reverse('auction_app:artwork-list')
    data = {
        'title': 'Test Artwork',
        'artist': 'Test Artist',
        'year_created': 2020,
        'dimensions': '10x10',
        'material': 'Canvas',
        'genre': 'Abstract',
        'description': 'Test Description',
        'minimum_bid': 100.00,
        'status': 'active'
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201

    # Verify the created artwork
    assert Artwork.objects.filter(title='Test Artwork').exists()

@pytest.mark.django_db
def test_artwork_retrieve(api_client, user):
    artwork = mixer.blend(Artwork)
    url = reverse('auction_app:artwork-detail', kwargs={'pk': artwork.pk})
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_artwork_update(api_client, user):
    artwork = mixer.blend(Artwork)
    url = reverse('auction_app:artwork-detail', kwargs={'pk': artwork.pk})
    data = {
        'title': 'Updated Title',
        'status': 'inactive'
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    artwork.refresh_from_db()
    assert artwork.title == 'Updated Title'
    assert artwork.status == 'inactive'

@pytest.mark.django_db
def test_artwork_delete(api_client, user):
    artwork = mixer.blend(Artwork)
    url = reverse('auction_app:artwork-detail', kwargs={'pk': artwork.pk})
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Artwork.objects.filter(pk=artwork.pk).exists()