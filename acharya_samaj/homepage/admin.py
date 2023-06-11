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



from .models import MessageOfBOD, Notice, Program

admin.site.register(MessageOfBOD)
admin.site.register(Notice)
admin.site.register(Program)

from .models import Service

admin.site.register(Service)