from django.db import models
from lists.models import Shoppinglist


class Item(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    shoppinglist = models.ForeignKey(Shoppinglist,
     related_name='shoppinglist', 
     on_delete=models.CASCADE)
    quantity = models.IntegerField( blank=False, unique=False)
    amount = models.IntegerField( blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
