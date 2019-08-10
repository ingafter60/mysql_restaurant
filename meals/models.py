from django.db import models

# Create your models here.

# Model name: Meals
class Meals(models.Model):
    ## Meals information
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people      = models.IntegerField()
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    preperation_time = models.IntegerField()
    image       = models.ImageField(upload_to='meals/')

    class Meta:
        verbose_name = "meal"
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name    
