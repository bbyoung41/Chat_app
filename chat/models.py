from django.db import models
# Create your models here.\

class NickNames(models.Model):
    Nickname = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.Nickname

class ChatGroup(models.Model):
    Group_name = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return self.Group_name
    
class ChatMessages(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(NickNames, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body

    class Meta:
        ordering = ['created']