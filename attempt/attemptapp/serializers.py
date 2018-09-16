from rest_framework import serializers
from attemptapp.models import Attempt


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('id', 'user_id', 'score')
        read_only_fields = ('id',)
