from django.db import models

# Create your models here.


# Database Structure With Name 'Details'
class Registration(models.Model):
    receiptNumber = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=20)
    year = models.CharField(max_length=2)
    email = models.EmailField()
    contact = models.DecimalField(decimal_places=0, max_digits=10)
    event = models.CharField(max_length=20)

    def __str__(self):
        return str(self.receiptNumber) + '-' + str(self.name)


class Participant(models.Model):
	receiptNumber = models.PositiveSmallIntegerField(unique=True)
	name = models.CharField(max_length=50)
	year = models.CharField(max_length=2)
	event = models.CharField(max_length=20)
	roomNumber = models.CharField(max_length=4)

	def __str__(self):
		return str(self.receiptNumber) + '-' + str(self.name)


class Certification(models.Model):
	receiptNumber = models.PositiveSmallIntegerField(unique=True)
	name = models.CharField(max_length=50)
	year = models.CharField(max_length=2)
	college = models.CharField(max_length=20)
	event = models.CharField(max_length=20)
	def __str__(self):
		return str(self.receiptNumber) + '-' + str(self.name)
