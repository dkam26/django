from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item


class CreateItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        """Save the post data when adding a new item."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated,
    #     IsOwner)
