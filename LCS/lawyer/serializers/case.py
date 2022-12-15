from datetime import timedelta
from rest_framework import serializers

from case.models import Case


class LawyerCaseRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = (
            "id",
            'state',
            'user',
            'title',
            'content',
            'issue_date', 
        )

