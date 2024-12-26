from django import forms
from chat.models import ChatMessages

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessages
        fields = ['body']  # Assuming you're only allowing the body of the message
