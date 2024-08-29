from django.db import models

ANSWER_TYPE_CHOICES = (
    ('boolean', 'Yes or No'),
    ('text', 'Short answer'),
    ('choices', 'Choices')
)

class Question(models.Model):
    question = models.TextField()
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.question