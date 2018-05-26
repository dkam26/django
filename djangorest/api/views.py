from django.shortcuts import render
from rest_framework import generics
from .serializers import ShoppinglistSerializer
from .models import Shoppinglist, User


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer