from django.db import models
from django.contrib.auth.models import User

class ImageCaption(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/')
    caption = models.TextField()
    date = models.DateField(auto_now_add=True)