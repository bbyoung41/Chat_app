from django.db import models
from django.contrib.auth.models import User
# Create your models here.\



class ChatGroup(models.Model):
    Group_name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)

    def __str__(self) -> str:
        return self.Group_name 
      
class ChatMessages(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']