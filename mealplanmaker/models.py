from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Carbs(models.Model):
	name = models.TextField(max_length=50)
	gfat = models.PositiveIntegerField(default=0)
	gcarb = models.PositiveIntegerField(default=0)
	gprotein = models.PositiveIntegerField(default=0)

class Fats(models.Model):
	name = models.TextField(max_length=50)
	gfat = models.PositiveIntegerField(default=0)
	gcarb = models.PositiveIntegerField(default=0)
	gprotein = models.PositiveIntegerField(default=0)

class Proteins(models.Model):
	name = models.TextField(max_length=50)
	gfat = models.PositiveIntegerField(default=0)
	gcarb = models.PositiveIntegerField(default=0)
	gprotein = models.PositiveIntegerField(default=0)

class Drinks(models.Model):
	name = models.TextField(max_length=50)
	gfat = models.PositiveIntegerField(default=0)
	gcarb = models.PositiveIntegerField(default=0)
	gprotein = models.PositiveIntegerField(default=0)

class Meals(models.Model):
	name = models.TextField(max_length=50)
	totalfat = models.PositiveIntegerField(default=0)
	totalcarb = models.PositiveIntegerField(default=0)
	totalprotein = models.PositiveIntegerField(default=0)
	calories = models.PositiveIntegerField(default=0)
	mealcreator = models.ForeignKey(User, on_delete=models.CASCADE)
	ingredients = models.TextField(max_length=400, default="")

class TDEE(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	calories = models.PositiveIntegerField(default=0)

class Weekly(models.Model):
	day = models.TextField(max_length=10)
	meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
	mealuser = models.ForeignKey(User, on_delete=models.CASCADE)