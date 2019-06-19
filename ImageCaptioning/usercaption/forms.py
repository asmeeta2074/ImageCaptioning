from .models import ImageCaption
from django.forms import ModelForm
from django import forms

class ImageCaptionForm(forms.ModelForm):
    class Meta:
        model = ImageCaption
        fields = ['image']