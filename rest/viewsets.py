from django.urls.conf import include
from rest_framework import viewsets
from rest.serializers import WorkSerializer
from rest.models import Work
from rest_framework.permissions import IsAuthenticated

class WorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    