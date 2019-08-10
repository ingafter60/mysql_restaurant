from django.db import models
from django.utils.text import slugify

# Create your models here.

# Model name: Meals
class Meals(models.Model):
    ## Meals information
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category    = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    people      = models.IntegerField()
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    preperation_time = models.IntegerField()
    image       = models.ImageField(upload_to='meals/')
    slug 		= models.SlugField(blank=True, null=True)

    # Create slug automatically based on name
    def save(self , *args , **kwargs):
      if not self.slug and self.name :
        self.slug = slugify(self.name)
      super(Meals , self).save(*args, **kwargs)

    # Making human readable name of meals from 'Mealss' to 'Meals'
    class Meta:
        verbose_name = "meal"
        verbose_name_plural = 'meals'

    # Displaying Melas's name in the admin panel
    def __str__(self):
        return self.name

# Model name: Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    # Making human readable name of meals from 'Mealss' to 'Meals'
    class Meta:
        verbose_name = "category"
        verbose_name_plural = 'categories'

    # Displaying Melas's name in the admin panel
    def __str__(self):
        return self.name
    