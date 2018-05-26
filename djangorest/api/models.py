from django.db import models
from django.db import models
from django.db import models


class User(models.Model):
    user = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Shoppinglist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
#