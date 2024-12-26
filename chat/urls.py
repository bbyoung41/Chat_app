from django.urls import include, path
from . import views

urlpatterns = [
    path('message/', views.add_message, name='add_message')

]
