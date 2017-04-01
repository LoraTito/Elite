from django.shortcuts import render

from main.models import HorseForSale
from main.models import ImageGallery


def index(request):
    return render(request, 'index.html')


def pansion(request):
    return render(request, 'pansion.html')


def about(request):
    return render(request, 'about.html')


def horses(request):
    data = {
        'horses': HorseForSale.objects.all(),
    }
    return render(request, 'horses.html', data)


def horse(request, horse_id):
    data = {
        'horse': HorseForSale.objects.get(id=horse_id),
    }
    return render(request, 'horse.html', data)


def gallery(request):
    data = {
        'gallery': ImageGallery.objects.all(),
    }
    return render(request, 'gallery.html', data)


def lessons(request):
    return render(request, 'lessons.html')
