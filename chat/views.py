from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from chat.models import ChatGroup, ChatMessages
from chatapp.forms import ChatMessageForm

# Create your views here.
def add_message(request):
    group = get_object_or_404(ChatGroup, id=1)
    current_user = request.user
    if request.method == 'POST':
      form = ChatMessageForm(request.POST)

    if form.is_valid():
        new_message = form.save(commit=False)
        new_message.group = group  # Associate message with the group
        new_message.author = current_user  # Associate message with the logged-in user
        new_message.save()
        return redirect('home')  # Redirect to the same chat view