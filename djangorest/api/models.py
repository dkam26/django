from django.db import models
from django.db import models
from django.db import models



class User(models.Model):
    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False, unique=True)
    Firstname = models.CharField(max_length=255, blank=False, unique=True, default='firstname')
    email = models.CharField(max_length=255, blank=False, unique=True, default='email')
    surname = models.CharField(max_length=255, blank=False, unique=True, default='surname')

    def __init__(self,user, surname, firstname ,email,password):
        self.username = user
        self.surname = surname
        self.firstname = firstname 
        self.email=email 
        self.password = password

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Shoppinglist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __init__(self,name):
        self.name = name
       
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
#