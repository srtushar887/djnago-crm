from django.db import models
from django.contrib.auth.models import User


class Adminuser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default='adminuser')
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='adminuser', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.first_name+' '+self.last_name

