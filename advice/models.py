from django.db import models


class Advice(models.Model):
    profile = models.ForeignKey('health_profile.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.profile.user.username
    
    class Meta:
        verbose_name_plural = 'Advices'
        ordering = ['-created']