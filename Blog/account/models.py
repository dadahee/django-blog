from django.db import models


# Create your models here.

class CustomUserModel(AbstractUser):
    GENDER = (
        ("M", "남자"),
        ("W", "여자"),
    )

    # 둘다 true -> 상관 없는 경우
    birthday = models.DateField(blank=True, null=True, input_formats=["%Y//%M//%D"])
    gender = models.CharField(blank=True, null=True)