from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.view_posts, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/', views.post, name='post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
]