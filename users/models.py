from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=250, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=250, verbose_name='фамилия', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verification_code = models.CharField(max_length=256, verbose_name='код проверки', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

