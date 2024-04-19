from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='log_in')
]