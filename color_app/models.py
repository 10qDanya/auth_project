from django.db import models
from django.contrib.auth.models import User
import random

class ColorChange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default='#FFFFFF')
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_random_color():
        return '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    

    @classmethod
    def get_last_change(cls):
        last_change = cls.objects.last()
        if last_change:
            return {
                'username': last_change.user.username,
                'color': last_change.color,
                'timestamp': last_change.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        return None