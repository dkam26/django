from rest_framework import serializers
from .models import Shoppinglist

class ShoppinglistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""



    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Shoppinglist
        fields = ('id', 'name', 'date_created')

