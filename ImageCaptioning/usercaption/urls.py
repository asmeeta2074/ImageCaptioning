from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from .views import SignupCreateView,ImageCaptionCreateView,ImageCaptionTemplateView,ImageCaptionGenerateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',SignupCreateView.as_view(),name ='signup'),
    path('',ImageCaptionCreateView.as_view(),name ='imagecaptioncreate'),
    path('<int:pk>/',ImageCaptionGenerateView.as_view(),name ='generatedcaption'),
    path('generated/',ImageCaptionTemplateView.as_view(),name ='imagecaption'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)