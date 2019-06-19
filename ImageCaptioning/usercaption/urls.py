from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from .views import SignupCreateView,ImageCaptionCreateView,ImageCaptionTemplateView

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',SignupCreateView.as_view(),name ='signup'),
    path('',ImageCaptionCreateView.as_view(),name ='imagecaptioncreate'),
    path('generated/',ImageCaptionTemplateView.as_view(),name ='imagecaption'),
]
