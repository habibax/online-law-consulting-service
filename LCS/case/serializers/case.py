from datetime import timedelta
from rest_framework import serializers

from case.models import Case


class CaseRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = (
            'state',
            'user',
            'title',
            'content',
            'issue_date', 
        )


class CaseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = (
            'title',
            'content',
        )
