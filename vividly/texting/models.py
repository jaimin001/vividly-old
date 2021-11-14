from django.db import models
from django.utils import tree
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    textMessage = models.TextField(max_length=1200 ,null=True, blank=True, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.textMessage

    class Meta:
        ordering = ('timestamp',)

