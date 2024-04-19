from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('chat/', views.Chat, name='chat')
]