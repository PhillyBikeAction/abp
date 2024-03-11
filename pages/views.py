from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def brand(request):
    return render(request, "brand-guidelines.html")
