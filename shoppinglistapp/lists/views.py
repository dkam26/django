from rest_framework import generics, permissions
from .serializers import ShoppinglistSerializer
from .models import Shoppinglist
from .permission import IsOwner
from rest_framework.authtoken.views import obtain_auth_token

class CreateShoppinglistView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
