from django import forms
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html
from django.forms import Media
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        html = super().render(name, value, final_attrs, renderer=renderer)
        return format_html(html)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'tinymce/tinymce' + extra + '.js',
            'tinymce-init.js',
        ]
        js = [reverse('admin:jsi18n')] + [settings.STATIC_URL + url for url in js]
        return forms.Media(js=js)
