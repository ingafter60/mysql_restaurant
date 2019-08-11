from django.db import models

# Create your models here.

# Model name: Reservation
class Reservation(models.Model):
	name 		= models.CharField(max_length=50)
	email 	= models.EmailField()
	phone 	= models.IntegerField()
	number_of_person = models.IntegerField()
	date 		= models.DateField()
	time 		= models.TimeField()

	# Displaying name in admin panle
	def __str__(self):
		return self.name
