from datetime import timedelta
from rest_framework import serializers

from case.models import Case


class AdminCaseRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = (
            "id",
            'state',
            'user',
            'lawyer',
            'title',
            'content',
            'issue_date', 
        )

