from django import forms
from .models import Applicant_new

class ApplicationForm(forms.ModelForm):
	admission_class = forms.CharField(max_length='2',widget = forms.NumberInput(),required=True)

	class Meta:
		model = Applicant_new
		fields = ['name','Fathername','Mothername','birthdate','birthreg','admission_class','religion','image','Present_addr','Permanent_addr','contact_no']