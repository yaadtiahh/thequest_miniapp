from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def info_center(request):
    return render(request, 'info_center.html')
