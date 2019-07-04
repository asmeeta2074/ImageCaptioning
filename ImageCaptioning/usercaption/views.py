from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,TemplateView,DetailView
from .models import ImageCaption
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageCaptionForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

class SignupCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usercaption/signup.html'
    success_url = '/'

class ImageCaptionCreateView(LoginRequiredMixin,CreateView):
    model = ImageCaption
    form_class = ImageCaptionForm


    def form_valid(self,form):
        form.instance.user = self.request.user
        print(type(form.instance.image))
        form.instance.caption = get_caption()
        return super(ImageCaptionCreateView,self).form_valid(form)

class ImageCaptionGenerateView(LoginRequiredMixin,DetailView):
    #template_name = 'usercaption/generatedcaption.html'
    model = ImageCaption

    def get_object(self,*args,**kwargs):
        pk = self.kwargs.get('pk')
        imagecaption = get_object_or_404(ImageCaption,pk=pk)
        return imagecaption
    def get_context_data(self,*args,**kwargs):
        context = {}
        context['imagecaption'] = self.get_object()
        return context



class ImageCaptionTemplateView(LoginRequiredMixin,TemplateView):
    model = ImageCaption
    template_name = 'usercaption/allgeneratedcaptions.html'

def get_caption():
    return "This"