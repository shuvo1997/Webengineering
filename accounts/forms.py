from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget = forms.EmailInput())
	phoneno = forms.CharField(max_length=254, required=True,label='Phone Number',widget = forms.TextInput())

	class Meta:
		model = User
		fields = ('username','email','phoneno','password1','password2')