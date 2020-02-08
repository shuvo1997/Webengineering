from django.db import models
from application.models import Applicant_new
from django.core.validators import MaxValueValidator,MinValueValidator

class payment(models.Model):
	applicant = models.OneToOneField(
		Applicant_new,
		on_delete = models.CASCADE,
		primary_key = True,
		)
	transaction_id = models.CharField(max_length=10,unique=True)
	is_verified = models.BooleanField(default=False)

	def __str__(self):
		return "%s" %self.transaction_id

class admission_result(models.Model):
	applicant = models.OneToOneField(
		payment,
		on_delete = models.CASCADE,
		primary_key = True,
		)
	bangla_marks = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
	english_marks = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
	math_marks = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])

	def __str__(self):
		return "%s" %self.applicant.name
