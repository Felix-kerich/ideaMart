from django.shortcuts import render

# Create your views here.

def mpesa_payment(request):
    return render(request, 'mpesa.html') 
