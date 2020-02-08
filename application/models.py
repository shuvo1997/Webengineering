from django.db import models
from django.contrib.auth.models import User

class Applicant_new(models.Model):
	name = models.CharField(max_length=100)
	Fathername = models.CharField(max_length=100)
	Mothername = models.CharField(max_length=100)
	birthdate = models.DateField()
	birthreg = models.CharField(max_length=17,unique=True)
	religion = models.CharField(max_length=100)
	Present_addr = models.CharField(max_length=1000)
	Permanent_addr = models.CharField(max_length=1000)
	contact_no = models.CharField(max_length=11)
	image = models.ImageField(upload_to='images/')	
	admission_class = models.IntegerField(default='0')
	belongs_to = models.ForeignKey(User,on_delete=models.CASCADE, related_name='applicant')

	def __str__(self):
		return "Applicant: %s Id: %d" %(self.name,self.id)