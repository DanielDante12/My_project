from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('member/',views.display, name='blog-member'),
]