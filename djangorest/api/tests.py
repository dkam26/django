from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import User, Shoppinglist

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.shoppinglist_name = "Write world class code"
        self.shoppinglist = Shoppinglist(name=self.shoppinglist_name)

    def test_model_can_create_a_shoppinglist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Shoppinglist.objects.count()
        self.shoppinglist.save()
        new_count = Shoppinglist.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_api_can_get_a_shoppinglist(self):
        """Test the api can get a given bucketlist."""
        shoppinglist = Shoppinglist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': shopping.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, shoppinglist)

    def test_api_can_update_shoppinglist(self):
        """Test the api can update a given bucketlist."""
        change_shoppinglist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': shoppinglist.id}),
            change_shoppinglist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_shoppinglist(self):
        """Test the api can delete a bucketlist."""
        shoppinglist = Shoppinglist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': shoppinglist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)