from datetime import datetime
from django.db import models

# Create your models here.
class LawyerRegisterDetail(models.Model):
	GENDER_CHOICES=(('Male','Male'),('Female','Female'),)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	city_name=models.CharField(max_length=100)
	company_name=models.CharField(max_length=200,blank=True)
	date_of_birth=models.DateField()
	gender=models.CharField(choices=GENDER_CHOICES,default=GENDER_CHOICES[0][0],max_length=6)
	email=models.EmailField()
	phone_number=models.CharField(max_length=20)
	state_bar_no=models.CharField(blank=True,max_length=50)
	bar_council_no=models.CharField(blank=True,max_length=50)
	#terms_conditions=models.BooleanField(default=False)
	register_time=models.DateTimeField(default=datetime.now,blank=True)
	def __str__(self):
		return self.email + " registered at " +self.register_time.strftime("%Y-%m-%d")


