from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class ImageCaption(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/')
    #caption = models.TextField(blank=True)
    #date = models.DateField(default = timezone.now)

    def get_absolute_url(self):
        return reverse('usercaption:imagecaption')