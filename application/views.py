from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Applicant_new
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
	return render(request,'home.html')

@login_required
def apply(request):
    
    if request.method == 'POST':
    	form = ApplicationForm(request.POST,request.FILES)

    	if form.is_valid():
            applicant = form.save(commit = False)
            applicant.belongs_to = request.user
            form.save()
            return redirect('home')
        
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form':form})

@login_required
def show_applicants(request):
    applicator = Applicant_new.objects.filter(belongs_to__username=request.user)

    context={'applicator':applicator}

    return render(request,'show_applicants.html',context)


def validate_contact_no(request):
    contact_no = request.GET.get('contact_no', None)
    data = {
        'is_taken': Applicant_new.objects.filter(contact_no__iexact=contact_no).exists()
    }
    return JsonResponse(data)

@login_required
def contact(request):
    return render(request,'contact.html')