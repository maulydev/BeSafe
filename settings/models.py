from django.db import models
from django.contrib.auth.models import User



class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_usage_limit = models.IntegerField(default=8)
    
    def __str__(self):
        return self.user.username