from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Username1", max_length=256)
    is_Organisation = models.BooleanField(default=False)

    def __str__(self):
        return self.name