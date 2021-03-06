from django.shortcuts import render, redirect
from .forms import *
from .pay import process_payment

# Create your views here.

def home(request):
    form = CustomPaymentForm()
    if request.method=='POST':
        form =CustomPaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return redirect(process_payment(amount, name, email))

    context = {'form': form}
    return render(request, 'payment.html', context)
