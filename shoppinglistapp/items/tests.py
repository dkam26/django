from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from lists.models import Shoppinglist
from .models import  Item


class ModelTestCase(TestCase):
    """This class defines the test suite for the shoppinglist and user model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.shoppinglist_data = {'name': 'Trousers'}
        self.response_shoppinglist = self.client.post(
            reverse('create'),
            self.shoppinglist_data,
            format="json")
        self.item_data = {'name':'jeans','quantity':3,'amount':45000,'shoppinglist':self.response_shoppinglist.data['id']}
        self.response_item = self.client.post(
            reverse('createItem'),
            self.item_data,
            format="json")

    def test_model_can_add_an_item(self):
        """Test the shoppinglist model can add a item."""
       
        self.assertEqual(self.response_item.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_item(self):
        """Test the api can get a given item."""
        item = Item.objects.get()
        response = self.client.get(
            reverse('itemdetails',
            kwargs={'pk': item.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, item)

    def test_api_can_update_an_item(self):
      
        item = Item.objects.get()
        change_item = {'name': 'khaki','quantity':4,'amount':50000,'shoppinglist':self.response_shoppinglist.data['id'] }
        res = self.client.put(
            reverse('itemdetails', kwargs={'pk': item.id}),
            change_item, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_item(self):
        """Test the api can delete an item."""
        item = Item.objects.get()
        response = self.client.delete(
            reverse('itemdetails', kwargs={'pk': item.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
