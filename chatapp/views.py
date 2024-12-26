from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from chat.models import *
from chatapp.forms import ChatMessageForm



def home(request, room_name):
   group, created = ChatGroup.objects.get_or_create(Group_name=room_name)
   group_details = ChatMessages.objects.filter(group=group)
   current_user = request.user
   if request.method == 'POST':
      form = ChatMessageForm(request.POST)

      if form.is_valid():
         new_message = form.save(commit=False)
         new_message.body = request.POST['message']
         new_message.group = group  # Associate message with the group
         new_message.author = current_user  # Associate message with the logged-in user
         new_message.save()

   else:
      form = ChatMessageForm()

   context = {
      'group_name' : group,
      'group_details' : group_details,
      'form' : form
   }

   return render(request, 'home.html', context)
    

def index(request):
   return render(request, 'index.html')