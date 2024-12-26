from django.http import HttpResponse
from django.shortcuts import render
from chat.models import *



def home(request):
   group_details = ChatMessages.objects.filter(group=1)

   context = {
      'group_details' : group_details
   }
   return render(request, 'home.html', context)
    