from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('mens/', views.mens, name='mens'),
    path('ladies/', views.ladies, name='ladies'),
    path('studio/', views.studio, name='studio'),
    path('contact/', views.contact, name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
