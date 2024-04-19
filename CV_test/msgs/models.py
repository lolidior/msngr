from datetime import datetime

from django.db import models
from django.urls import reverse


class msgs(models.Model):
    send = models.CharField('Отправитель', max_length=200, default='asd')
    take = models.CharField('Приниматель', max_length=20, default='asd')
    msg_txt = models.CharField('Сообщение', max_length=250)
    send_date = models.CharField('Дата отправки', max_length=100)

    def __str__(self):
        return self.msg_txt

    def get_absolute_url(self):
        return reverse('chat_view', kwargs={'slug': self.take})