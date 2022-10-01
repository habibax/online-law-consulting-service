from django.db import models

from common.common_models import BaseModel


class AdminProfile(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(
        "acc.User", on_delete=models.CASCADE, related_name="admin_profile"
    )
