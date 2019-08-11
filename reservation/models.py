# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# # Create your models here.

# # Model name: Reservation
# class Reservation(models.Model):
# 	name 		= models.CharField(max_length=50)
# 	email 	= models.EmailField()
# 	phone 	= PhoneNumberField()
# 	number_of_persons = models.IntegerField()
# 	Date 		= models.DateField()
# 	time 		= models.TimeField()

# 	# Displaying name in admin panle
# 	def __str__(self):
# 		return self.name

from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return self.name