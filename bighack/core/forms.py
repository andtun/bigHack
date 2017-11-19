from django import forms
from django.forms import formset_factory
from .models import *

__all__ = ['ApplicationForm', 'ImageForm', 'ImageFormSet']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['title']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file']


ImageFormSet = formset_factory(
    ImageForm,
    extra=2,
    min_num=1,
    validate_min=True
)
