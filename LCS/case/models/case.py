from datetime import timedelta
from django.db import models
from django.utils.timezone import now

from common.common_models import BaseModel


class Case(BaseModel):
    class State(models.TextChoices):
        PENDING_ADMIN = ("pending_admin",)
        PENDING_LAWYER = ("pending_lawyer",)
        ACCEPTED = ("accepted",)
        REJECTED = ("rejected",)

    state = models.CharField(
        max_length=20, default=State.PENDING_ADMIN, null=False, choices=State.choices
    )
    user = models.ForeignKey("acc.User", on_delete=models.CASCADE, related_name="case_user")
    lawyer = models.ForeignKey("acc.User", on_delete=models.CASCADE, related_name="case_lawyer") 

    title = models.CharField(max_length=225, null=False)
    content = models.TextField()  
    issue_date = models.DateField(null=False, default=now)

    

