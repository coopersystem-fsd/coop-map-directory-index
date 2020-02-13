from django.db import models
from django.contrib.gis.db import models
from accounts.models import User
from django.contrib.postgres.fields import HStoreField
from django.urls import reverse
from django.db.models import Manager as GeoManager


class Category(models.Model):
    name = models.CharField(blank=False, max_length=255, unique=True)
    description = models.CharField(blank=True, default='', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(blank=False, max_length=255, unique=True)
    description = models.CharField(blank=True, default='', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(blank=False, max_length=255, unique=True)
    description = models.CharField(blank=True, default='', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, default='')
    url = models.CharField(blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, default='')
    url = models.CharField(blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, default='')
    address = models.CharField(blank=True, default='', max_length=255)
    city = models.CharField(blank=True, default='', max_length=255)
    state = models.CharField(blank=True, default='', max_length=255)
    postal_code = models.CharField(blank=True, default='', max_length=255)
    country = models.CharField(blank=True, default='', max_length=3)
    email = models.CharField(blank=True, default='', max_length=255)
    url = models.CharField(blank=True, default='', max_length=255)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    geom = models.PointField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    activities = models.ManyToManyField(Activity)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}, {}'.format(self.name, self.city)


class User(User):
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        ordering = ['last_name', 'first_name']
