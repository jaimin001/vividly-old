from django.db import models
from django.utils import tree
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(name='pfp')

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='receiver')
    textMessage = models.TextField(max_length=1200 ,null=True, blank=True, default=None)
    file = models.FileField(upload_to=None, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.textMessage

    class Meta:
        ordering = ('timestamp',)

