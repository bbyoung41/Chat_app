# Generated by Django 5.1.4 on 2024-12-19 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NickNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nickname', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chat.chatgroup')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.nicknames')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]