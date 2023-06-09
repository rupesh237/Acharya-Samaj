from django.contrib import admin
from .models import Slider

# Register your models here.

admin.site.register(Slider)


from .models import MessageOfBOD, Notices, Programs

admin.site.register(MessageOfBOD)
admin.site.register(Notices)
admin.site.register(Programs)

from .models import Services

admin.site.register(Services)