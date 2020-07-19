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

class Opportunites(models.Model):
    name = models.CharField(unique=True,null=False, max_length=64)
    url = models.CharField(unique=True, null=False, max_length=256)
    description = models.CharField(null=False, max_length=2500)
    date = models.DateField(null=False)
    category = models.CharField(null=False, max_length=32)
    likes = models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Opportunites, on_delete=models.CASCADE)
    value= models.IntegerField(default=0)
    def __str__(self):
       return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
