from django.db import models

from common.common_models import BaseModel
from django.core.validators import MinLengthValidator


class UserProfile(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    # national_code = models.IntegerField(null=True,max_length=10, validators=[MinLengthValidator(10)])
    # city= models.CharField(null=False, max_length=255)
    user = models.OneToOneField(
        "acc.User", on_delete=models.CASCADE, related_name="user_profile"
    )
    def __str__(self) -> str:
        return self.user.email