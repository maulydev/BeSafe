from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    avg_screen_time = models.DecimalField(max_digits=10, decimal_places=2, help_text='Hours')
    health_story = models.TextField(blank=True, default="no-story")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username