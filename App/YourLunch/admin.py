from django.contrib import admin
from .models import User, Restaurant, Menu, Dish, Employee

# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(Employee)

