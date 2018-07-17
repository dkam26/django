from rest_framework import serializers
from .models import Shoppinglist
from django.contrib.auth.models import User

class ShoppinglistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Shoppinglist
        fields = ('id', 'name', 'date_created','owner')

