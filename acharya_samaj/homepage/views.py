from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.conf import settings

from .models import Slider, MessageOfBOD, Notice, Program, Service

# from django.shortcuts import redirect
# from django.utils.translation import activate, LANGUAGE_SESSION_KEY


# Create your views here.
def index(request):
    return render(request, 'homepage/home.html',{
        "slides": Slider.objects.all(),
        "notices": Notice.objects.all(),
        "programs": Program.objects.all()
    })


def contact(request):
    return render(request, 'homepage/contact.html')


def home(request):
    return render(request, 'homepage/home.html',{
        "slides": Slider.objects.all(),
        "notices": Notice.objects.all(),
        "programs": Program.objects.all()
    })


def notice(request):
    return render(request, 'homepage/notice.html',{
        "notices": Notice.objects.all()
    })


def about(request):
    return render(request, 'homepage/about.html',{
        "abouts": Service.objects.all()
    })


# from django.utils.translation import activate, get_language
from django.utils.translation import get_language, activate, gettext_lazy as _


def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in [lang[0] for lang in settings.LANGUAGES]:
            request.session[settings.LANGUAGE_SESSION_KEY] = language
            activate(language)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


