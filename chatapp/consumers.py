import json
from channels.consumer import SyncConsumer

from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from chat.models import ChatGroup
from chat.models import *
from channels.db import database_sync_to_async

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name'] 
        self.chatroom = ChatGroup.objects.get_or_create(Group_name=self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_name, 
            self.channel_name
        )
        self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # To reject the connection, call:
        # self.close()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']
        
        #todo broadcast to all people in a specific group for the javascript in frontend to receive and display it to everyone in the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type':'chat_message',
                'message':message,
                'username':user
            }
        )

        #todo save to database
        self.save_message(self.room_name, user, message)
        print('Message:', message)


    def chat_message(self, event):
        message = event['message']
        user = event['username']

        self.send(text_data=json.dumps({
            'type':'chat_message',
            'message':message,
            'user': user,
        }))  

    @database_sync_to_async
    def save_message(self, group_name, user_name, message):
        user = User.objects.get(user_name=user_name)
        group = ChatGroup.objects.get(Group_name=group_name)
        ChatMessages.objects.create(group=group, author=user,body=message)

