from django import forms
from .models import payment,admission_result

class PaymentForm(forms.ModelForm):
	class Meta:
		model = payment
		fields = ['applicant','transaction_id']