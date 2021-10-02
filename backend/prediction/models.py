from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class model_image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    symptom = models.CharField(max_length=100)
    probability = models.CharField(max_length=80)
    image = models.CharField(max_length=700)
