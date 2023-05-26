from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')


def contact(request):
    return render(request, 'homepage/contact.html')


def home(request):
    return render(request, 'homepage/home.html')


def notice(request):
    return render(request, 'homepage/notice.html')


def about(request):
    return render(request, 'homepage/about.html')