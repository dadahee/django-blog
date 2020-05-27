from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings


# Create your models here.

class CustomUserModel(AbstractUser):
    GENDER = (
        ("M", "남자"),
        ("W", "여자"),
    )
    # 둘다 true -> 상관 없는 경우
    profile = models.ImageField(upload_to='account/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER)