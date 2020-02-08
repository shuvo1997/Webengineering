from django.shortcuts import render,redirect
from .forms import PaymentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View

from schooladmit.utils import render_to_pdf 

@login_required
def payment(request):
    if request.method == 'POST':
    	form = PaymentForm(request.POST)

    	if form.is_valid():
            paid = form.save(commit = False)
            form.save()
            return redirect('apply_done')
        
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form':form})

def GeneratePdf(request):
		data = {
			'today': 'asdsa', 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
		}
		pdf = render_to_pdf('admit.html',data)
		return HttpResponse(pdf, content_type='application/pdf')