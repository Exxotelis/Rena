from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.


def index(request):
    # Use STATICFILES_DIRS to specify the directory containing your images
    image_dir = os.path.join(
        settings.STATICFILES_DIRS[0], 'images', 'portfolio')
    images = os.listdir(image_dir)
    return render(request, 'index.html', {'images': images})


def mens(request):
    return render(request, 'mens.html')


def ladies(request):
    return render(request, 'ladies.html')


def studio(request):
    return render(request, 'studio.html')


def contact(request):
    return render(request, 'contact.html')
