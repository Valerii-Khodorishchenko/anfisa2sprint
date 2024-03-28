from django.contrib import admin

# Из модуля models импортируем модуль Category...
from .models import Category, IceCream, Topping, Wrapper

# Register your models here.

# ...и регистрируем её в админке:
admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream)
