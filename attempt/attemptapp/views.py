from rest_framework import viewsets
from attemptapp.models import Attempt
from attemptapp.serializers import AttemptSerializer

class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
