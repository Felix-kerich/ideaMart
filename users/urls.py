from django.urls import path
from django.conf.urls import handler404

from . import views


handler404 = views.custom_404_view

urlpatterns = [
    path('', views.home_view, name='home_logout'), 
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register_view, name='register'),
    path('profile/<str:username>/update_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('update/', views.update_profile, name='update_profile'),
    path('user/<str:username>/', views.view_profile, name='view_profile'),
    path('profile/<str:username>/toggle-follow/', views.toggle_follow, name='toggle_follow'),
    path('messages/conversation/<int:user_id>/', views.conversation_view, name='conversation_view'),
    path('messages/send/', views.send_message, name='send_message'),
    path('users/', views.user_list, name='user_list'),
    path('users_messages/', views.messages_user_list, name='user_list_messages'),   
    path('logout/', views.user_logout, name='logout'), 
    
]