from django.test import TestCase, Client
from django.urls import reverse


class StoreViewTests(TestCase):
    """Test store application views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_home_page_loads(self):
        """Test that home page returns 200 status."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_products_page_loads(self):
        """Test that products page returns 200 status."""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        """Test that about page returns 200 status."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_user_redirect_route_loads(self):
        """Test that user redirect route responds."""
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 302)

