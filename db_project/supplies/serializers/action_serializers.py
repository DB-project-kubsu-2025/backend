# supplies/serializers/action_serializers.py
from rest_framework import serializers


class DecisionSerializer(serializers.Serializer):
    decision_comment = serializers.CharField(required=False, allow_blank=True, max_length=300)