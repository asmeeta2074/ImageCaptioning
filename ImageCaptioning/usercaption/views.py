from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,TemplateView,DetailView, ListView
from .models import ImageCaption
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageCaptionForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
from .ImageCaption import get_caption

# def get_caption(x):
#     return "Caption Generated once"

class SignupCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usercaption/signup.html'
    success_url = '/'

class ImageCaptionCreateView(LoginRequiredMixin,CreateView):
    model = ImageCaption
    form_class = ImageCaptionForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        caption = get_caption(form.instance.image)
        caption = caption.split("\n")
        form.instance.caption1 = caption[0]
        form.instance.caption2 = caption [1]
        form.instance.caption3 =caption [2]
        return super(ImageCaptionCreateView,self).form_valid(form)

class ImageCaptionGenerateView(LoginRequiredMixin,DetailView):
    model = ImageCaption

    def get_object(self,*args,**kwargs):
        pk = self.kwargs.get('pk')
        imagecaption = get_object_or_404(ImageCaption,pk=pk)
        return imagecaption
    def get_context_data(self,*args,**kwargs):
        context = {}
        context['imagecaption'] = self.get_object()
        return context

class ImageCaptionTemplateView(LoginRequiredMixin,ListView):
    model = ImageCaption
    template_name = 'usercaption/allgeneratedcaptions.html'
