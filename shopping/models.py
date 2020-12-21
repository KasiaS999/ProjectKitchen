from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToBuy(models.Model):
    text = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
