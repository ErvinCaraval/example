from django.test import TestCase
from django.utils import timezone
from .models import Auction, Artwork, Customer, Bid, Admin
from django.core.exceptions import ValidationError

class TestModels(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(full_name="John Doe", email="john@example.com", phone="123456789", document_type="ID", document_number="123456789")
        self.auction = Auction.objects.create(auction_name="Test Auction", auction_description="Test Description", start_date=timezone.now(), end_date=timezone.now())
        self.artwork = Artwork.objects.create(auction=self.auction, title="Test Artwork", artist="Test Artist", year_created=2022, dimensions="10x10", material="Oil on Canvas", genre="Abstract", description="Test Description", minimum_bid=100.00)
        self.admin = Admin.objects.create(email="admin@example.com", password="adminpassword")

    def test_auction_creation(self):
        auction = Auction.objects.get(auction_name="Test Auction")
        self.assertEqual(auction.auction_name, "Test Auction")
        self.assertEqual(auction.auction_description, "Test Description")
        self.assertTrue(auction.start_date)
        self.assertTrue(auction.end_date)
        self.assertEqual(auction.status, "active")

    def test_artwork_creation(self):
        artwork = Artwork.objects.get(title="Test Artwork")
        self.assertEqual(artwork.title, "Test Artwork")
        self.assertEqual(artwork.artist, "Test Artist")
        self.assertEqual(artwork.year_created, 2022)
        self.assertEqual(artwork.dimensions, "10x10")
        self.assertEqual(artwork.material, "Oil on Canvas")
        self.assertEqual(artwork.genre, "Abstract")
        self.assertEqual(artwork.description, "Test Description")
        self.assertEqual(artwork.minimum_bid, 100.00)
        self.assertEqual(artwork.status, "active")

    def test_customer_creation(self):
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.full_name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone, "123456789")
        self.assertEqual(customer.document_type, "ID")
        self.assertEqual(customer.document_number, "123456789")

    def test_admin_creation(self):
        admin = Admin.objects.get(email="admin@example.com")
        self.assertEqual(admin.email, "admin@example.com")
        self.assertNotEqual(admin.password, "adminpassword")
        self.assertTrue(admin.password)

    def test_bid_creation(self):
        bid = Bid.objects.create(auction=self.auction, artwork=self.artwork, customer=self.customer, bid_value=200.00, bid_timestamp=timezone.now())
        self.assertEqual(bid.auction, self.auction)
        self.assertEqual(bid.artwork, self.artwork)
        self.assertEqual(bid.customer, self.customer)
        self.assertEqual(bid.bid_value, 200.00)
        self.assertTrue(bid.bid_timestamp)

    def test_invalid_auction_end_date(self):
        with self.assertRaises(ValidationError):
            auction = Auction.objects.create(auction_name="Invalid Auction", auction_description="Test Description", start_date=timezone.now(), end_date=timezone.now()-timezone.timedelta(days=1))
            auction.clean()
