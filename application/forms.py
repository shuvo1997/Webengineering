from django import forms
from .models import Applicant_new

class ApplicationForm(forms.ModelForm):
	name = forms.CharField(label = 'Applicants Name')
	Fathername = forms.CharField(label = 'Father\'s name')
	birthdate = forms.CharField(widget = forms.DateInput(),help_text='Format:YYYY-MM-DD')
	admission_class = forms.CharField(max_length='2',widget = forms.NumberInput(),required=True)


	class Meta:
		model = Applicant_new
		fields = ['name','Fathername','Mothername','birthdate','birthreg','admission_class','religion','image','Present_addr','Permanent_addr','contact_no']