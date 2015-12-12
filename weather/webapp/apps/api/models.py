
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import UserManager
from datetime import datetime
from datetime import date


class City(models.Model):
    """
    """
    name = models.CharField(max_length=254)