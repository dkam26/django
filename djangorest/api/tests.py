from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import User,Shoppinglist

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.shoppinglist_name = "Write world class code"
        self.shoppinglist = Shoppinglist(name=self.shoppinglist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Shoppinglist.objects.count()
        self.shoppinglist.save()
        new_count = Shoppinglist.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.client = APIClient()
        self.shoppinglist_data = {'name': 'shirts'}
        self.response = self.client.post(
            reverse('create'),
            self.shoppinglist_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
