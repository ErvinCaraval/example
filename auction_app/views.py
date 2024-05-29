import unittest
from unittest.mock import Mock
from rest_framework.test import APIRequestFactory
from .views import AuctionViewSet, ArtworkViewSet, CustomerViewSet, BidViewSet, AdminViewSet

class TestAuctionViewSet(unittest.TestCase):
    def setUp(self):
        self.view = AuctionViewSet()
        self.view.queryset = Mock()
        self.view.serializer_class = Mock()

    def test_queryset(self):
        self.view.queryset.all.assert_called_once()

class TestArtworkViewSet(unittest.TestCase):
    def setUp(self):
        self.view = ArtworkViewSet()
        self.view.queryset = Mock()
        self.view.serializer_class = Mock()

    def test_queryset(self):
        self.view.queryset.all.assert_called_once()

class TestCustomerViewSet(unittest.TestCase):
    def setUp(self):
        self.view = CustomerViewSet()
        self.view.queryset = Mock()
        self.view.serializer_class = Mock()
        self.request = APIRequestFactory().get('/')
        self.request.user = Mock(is_staff=False, id=1)

    def test_get_queryset_staff(self):
        self.request.user.is_staff = True
        queryset = self.view.get_queryset()
        self.view.queryset.all.assert_called_once()

    def test_get_queryset_non_staff(self):
        queryset = self.view.get_queryset()
        self.view.queryset.filter.assert_called_once_with(id=1)

class TestBidViewSet(unittest.TestCase):
    def setUp(self):
        self.view = BidViewSet()
        self.view.queryset = Mock()
        self.view.serializer_class = Mock()
        self.request = APIRequestFactory().get('/')
        self.request.user = Mock(is_staff=False)

    def test_get_queryset_staff(self):
        self.request.user.is_staff = True
        queryset = self.view.get_queryset()
        self.view.queryset.all.assert_called_once()

    def test_get_queryset_non_staff(self):
        self.request.user.is_staff = False
        self.request.user.id = 1
        queryset = self.view.get_queryset()
        self.view.queryset.filter.assert_called_once_with(customer=1)

class TestAdminViewSet(unittest.TestCase):
    def setUp(self):
        self.view = AdminViewSet()
        self.view.queryset = Mock()
        self.view.serializer_class = Mock()

    def test_queryset(self):
        self.view.queryset.all.assert_called_once()

if __name__ == '__main__':
    unittest.main()
