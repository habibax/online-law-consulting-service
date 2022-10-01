from django.db import models

from common.common_models import BaseModel


class UserProfile(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    btc_wallet_address = models.CharField(max_length=255, null=True)
    network_wallet_address = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(
        "acc.User", on_delete=models.CASCADE, related_name="user_profile"
    )
