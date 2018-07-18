from django.db import models


class Shoppinglist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
    
