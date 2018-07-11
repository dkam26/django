from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import User, Shoppinglist


class ModelTestCase(TestCase):
    """This class defines the test suite for the shoppinglist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user = {'user': 'deo','password':'1234','email':'deo@gmail.com'}
        self.user_response = self.client.post(
            reverse('createuser'),
            self.user,
            format="json")
        self.shoppinglist_data = {'name': 'Trousers','owner':self.user_response.data['id']}
        self.response = self.client.post(
            reverse('create'),
            self.shoppinglist_data,
            format="json")

    def test_model_can_create_a_shoppinglist(self):
        """Test the shoppinglist model can create a shoppinglist."""
       
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_model_can_create_a_user(self):
        """Test the User model can create a user."""
        self.assertEqual(self.user_response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_shoppinglist(self):
        """Test the api can get a given shoppinglist."""
        shoppinglist = Shoppinglist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': shoppinglist.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, shoppinglist)

    def test_api_can_update_shoppinglist(self):
        """Test the api can update a given shoppinglist."""
        shoppinglist = Shoppinglist.objects.get()
        change_shoppinglist = {'name': 'Something new','owner':self.user_response.data['id'] }
        res = self.client.put(
            reverse('details', kwargs={'pk': shoppinglist.id}),
            change_shoppinglist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_shoppinglist(self):
        """Test the api can delete a shoppinglist."""
        shoppinglist = Shoppinglist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': shoppinglist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

