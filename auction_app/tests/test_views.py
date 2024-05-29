import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import Auction

@pytest.mark.django_db
def test_list_auctions():
    """
    Prueba que la lista de subastas sea accesible.
    """
    client = APIClient()

    # Crear algunas instancias de subastas para probar
    Auction.objects.create(title='Subasta 1', description='Descripción de la subasta 1', start_price=100)
    Auction.objects.create(title='Subasta 2', description='Descripción de la subasta 2', start_price=200)

    # Realizar una solicitud GET a la vista de la API
    url = reverse('auction-list')
    response = client.get(url)

    # Verificar que la solicitud haya sido exitosa (código de estado 200)
    assert response.status_code == status.HTTP_200_OK

    # Verificar que los datos devueltos son correctos
    auctions = Auction.objects.all()
    assert len(response.data) == auctions.count()
    for auction_data, auction in zip(response.data, auctions):
        assert auction_data['title'] == auction.title
        assert auction_data['description'] == auction.description
        assert auction_data['start_price'] == auction.start_price
