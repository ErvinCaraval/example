from django.test import TestCase
from auction_app.models import Customer


import os

# Imprimir el valor de cada variable de entorno
print("DB_NAME:", os.environ.get('DB_NAME'))
print("DB_USER:", os.environ.get('DB_USER'))
print("DB_PASSWORD:", os.environ.get('DB_PASSWORD'))
print("DB_HOST:", os.environ.get('DB_HOST'))
print("DB_PORT:", os.environ.get('DB_PORT'))

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos iniciales para todas las pruebas del modelo
        Customer.objects.create(
            full_name='Juan Perez',
            email='juan@example.com',
            phone='1234567890',
            document_type='DNI',
            document_number='12345678'
        )

    def test_full_name_label(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_email_label(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_phone_label(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_document_type_label(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('document_type').verbose_name
        self.assertEqual(field_label, 'document type')

    def test_document_number_label(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('document_number').verbose_name
        self.assertEqual(field_label, 'document number')

    def test_string_representation(self):
        customer = Customer.objects.get(customer_id=1)
        self.assertEqual(str(customer), customer.full_name)
