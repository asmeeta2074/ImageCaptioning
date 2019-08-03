from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from django.utils import timezone

class ImageCaption(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',null=True)
    caption1 = models.TextField(blank=True)
    caption2 = models.TextField(blank=True)
    caption3 = models.TextField(blank=True)
    date = models.DateField(default = timezone.now)

    def get_absolute_url(self):
        return reverse('generatedcaption',kwargs={'pk':self.pk})