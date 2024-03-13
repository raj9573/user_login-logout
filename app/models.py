from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class userprofile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics/')
