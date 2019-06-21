from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,TemplateView,DetailView
from .models import ImageCaption
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageCaptionForm
from django.http import HttpResponse
class SignupCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usercaption/signup.html'
    success_url = '/'

class ImageCaptionCreateView(LoginRequiredMixin,CreateView):
    model = ImageCaption
    form_class = ImageCaptionForm
    # def  post(self,request, *args, **kwargs):
    #     form = ImageCaptionForm(request.POST,request.FILES)
    #     #form.instance.user = self.request.user
    #     if form.is_valid():
    #         print("Form is valid")
    #     else:
    #         print("form is invalid")
    #         return HttpResponse("Failed")
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("Valid Valid Valid")
        return super().form_valid(form)


class ImageCaptionGenerateView(LoginRequiredMixin,DetailView):
    template_name = 'usercaption/generatedcaption.html'


class ImageCaptionTemplateView(LoginRequiredMixin,TemplateView):
    model = ImageCaption
    template_name = 'usercaption/allgeneratedcaptions.html'
