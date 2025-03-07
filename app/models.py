from django.db import models
from cloudinary.models import CloudinaryField

class my_user(models.Model):
    username = models.CharField(max_length=255, )
    password = models.CharField(max_length=255)
    email = models.EmailField()
    profile_image = CloudinaryField(folder='media/user_profile')  # Correct folder path
