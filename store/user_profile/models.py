from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    photo = models.ImageField(blank=True,upload_to='profile/photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=55)

    def __str__(self):
        return self.first_name


