from django.contrib import admin

from .models import User, Carbs, Fats, Proteins, Drinks, Meals, TDEE

# Register your models here.

admin.site.register(User)
admin.site.register(Carbs)
admin.site.register(Fats)
admin.site.register(Proteins)
admin.site.register(Drinks)
admin.site.register(Meals)
admin.site.register(TDEE)
