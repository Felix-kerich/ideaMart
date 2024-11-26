from django.urls import path

from . import views

urlpatterns = [

    path('marketplace/', views.marketplace, name='marketplace'),
    path('create_product/', views.create_product, name='create_product'),
    path('post_product/', views.post_product, name='post_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

]