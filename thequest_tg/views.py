from django.shortcuts import render


def map(request):
    return render(request, 'map.html',  {'active_page': 'map'})

def info_center(request):
    return render(request, 'info_center.html',{'active_page': 'info_center'})

def profile(request):
    return render(request, 'profile.html',{'active_page': 'profile'})

