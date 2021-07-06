from rest_framework import viewsets
from rest.serializers import WorkSerializer
from rest.models import Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    