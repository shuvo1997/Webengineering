from django import forms
from .models import Applicant_new

class ApplicationForm(forms.ModelForm):
	classes = (
		(11,'1'),
		(12,'2'),
		(13,'3'),
		(14,'4'),
		(15,'5'),
		(16,'6'),
		)
	religions = (
		(11,'Islam'),
		(12,'Hindu'),
		(13,'Buddhist'),
		(14,'Other'),
		)
	name = forms.CharField(label = 'Applicants Name')
	Fathername = forms.CharField(label = 'Father\'s name')
	Mothername = forms.CharField(label = 'Mother\'s name')
	birthdate = forms.DateField(help_text='Format:YYYY-MM-DD')
	admission_class = forms.ChoiceField(choices = classes)
	religion = forms.ChoiceField(choices = religions)

	class Meta:
		model = Applicant_new
		fields = ['name','Fathername','Mothername','birthdate','birthreg','admission_class','religion','image','Present_addr','Permanent_addr','contact_no']