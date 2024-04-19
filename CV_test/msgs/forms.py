from django.http import request

from main.models import User
from .models import msgs
from django.forms import ModelForm, TextInput

class msg_send(ModelForm):

    class Meta:

        model = msgs
        fields = ['send', 'take', 'msg_txt', 'send_date']

