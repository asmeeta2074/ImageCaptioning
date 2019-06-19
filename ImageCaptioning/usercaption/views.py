from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,TemplateView
from .models import ImageCaption
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageCaptionForm
class SignupCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usercaption/signup.html'
    success_url = '/'

class ImageCaptionCreateView(LoginRequiredMixin ,CreateView):
    model = ImageCaption
    form_class = ImageCaptionForm

class ImageCaptionTemplateView(LoginRequiredMixin,TemplateView):
    model = ImageCaption
    template_name = 'usercaption/generatedcaptions.html'
