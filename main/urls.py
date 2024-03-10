from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mens/', views.mens, name='mens'),
    path('ladies/', views.ladies, name='ladies'),
    path('studio/', views.studio, name='studio'),
    path('contact/', views.contact, name='contact'),

]
