from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('done', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'
