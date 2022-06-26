from django.db import models

class Passenger(models.Model):

	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	# status = 
	registered_date = models.DateTimeField(auto_now=True)
	# distance = models.ManyToManyField()

	def __str__(self) -> str:
		return self.name

class PassengerTrips(models.Model):

	passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
	total_distance = models.IntegerField()
	start_time = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.start_time