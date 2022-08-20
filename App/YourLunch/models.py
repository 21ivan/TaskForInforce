from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)

    REQUIRED_FIELDS = ['first_name', 'email']

    def __str__(self):
        return self.email


class Dish(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field'
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    dishes = models.ManyToManyField(Dish)
    day = models.OneToOneField(Day,
                               on_delete=models.CASCADE,
                               primary_key=True)

    def __str__(self):
        return self.day.name


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    admin_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    working_hours = models.CharField(max_length=200)
    menu = models.OneToOneField(Menu,
                                on_delete=models.CASCADE,
                                primary_key=True, )
    rating = models.FloatField()

    def __str__(self):
        return "the restaurant %s " % self.name
