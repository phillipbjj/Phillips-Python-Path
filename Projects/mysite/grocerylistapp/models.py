from django.db import models
# Create your models here.

class Food(models.Model):
    food_text = models.CharField(max_length=200)
    foodadd_date = models.DateTimeField("date added")
    def __str__(self):
        return self.food_text
    
class NonFood(models.Model):
    nonfood_text = models.CharField(max_length=200)
    nonfoodadd_date = models.DateTimeField("date added")
    def __str__(self):
        return self.nonfood_text

