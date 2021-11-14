from django.db import models
from django.utils import tree

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, blank=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    textMessage = models.TextField(max_length=1200 ,null=True, blank=True, default=None)
    file = models.FileField(upload_to=None, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.textMessage

    class Meta:
        ordering = ('timestamp',)

