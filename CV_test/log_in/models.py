from django.contrib.auth.models import AbstractUser
from django.db import models


class auth(models.Model):
    login = models.CharField('Login', max_length=20)
    password = models.CharField('Password', max_length=20)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'
