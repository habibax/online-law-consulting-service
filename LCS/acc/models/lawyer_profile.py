from django.db import models

from common.common_models import BaseModel
from django.core.validators import MinLengthValidator


class LawyerProfile(BaseModel):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    # national_code = models.IntegerField(null=False,max_length=10, validators=[MinLengthValidator(10)])
    expert= models.CharField(max_length=255, null=True)
    city= models.CharField(null=False, max_length=255)
    user = models.OneToOneField(
        "acc.User", on_delete=models.CASCADE, related_name="lawyer_profile"
    )
