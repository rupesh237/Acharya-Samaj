from django import forms
from django.contrib import admin
from .models import Slider
from django.db import models

# Register your models here.

# from .widgets import TinyMCEWidget
from tinymce.widgets import TinyMCE
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinymce-init.js')



from .models import MessageOfBOD, Notices, Programs

admin.site.register(MessageOfBOD)
admin.site.register(Notices)
admin.site.register(Programs)

from .models import Services

admin.site.register(Services)