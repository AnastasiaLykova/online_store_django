from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)
    verify_key = models.CharField(max_length=35, verbose_name='ключ верификации', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='подтвержден')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
