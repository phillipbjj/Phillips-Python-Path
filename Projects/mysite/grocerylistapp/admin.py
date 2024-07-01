from django.contrib import admin

# Register your models here.
from .models import Food, NonFood

admin.site.register(Food)
admin.site.register(NonFood)