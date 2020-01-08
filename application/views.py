from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Applicant_new
from django.contrib.auth.models import User

def home(request):
	return render(request,'home.html')

def apply(request):
    
    user = User.objects.first()

    if request.method == 'POST':
    	form = ApplicationForm(request.POST,request.FILES)

    	if form.is_valid():
            applicant = form.save(commit = False)
            applicant.belongs_to = user
            form.save()
            return redirect('home')
        
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form':form})

def show_applicants(request):
    applicant1 = Applicant_new.objects.all()

    context={'applicant1':applicant1}

    return render(request,'show_applicants.html',context)