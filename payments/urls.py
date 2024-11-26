from django.urls import path

from . import views

urlpatterns = [
    path('make_mpesa_payment/', views.mpesa_payment, name='mpesa_payment'), 

]