from django.test import TestCase, Client
from django.urls import reverse


class StoreViewTests(TestCase):
    """Test store application views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_index_page_loads(self):
        """Test that index page returns 200 status."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_shop_page_loads(self):
        """Test that shop page returns 200 status."""
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        """Test that about page returns 200 status."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        """Test that contact page returns 200 status."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

