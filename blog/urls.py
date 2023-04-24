from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('post', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-details'),
]
