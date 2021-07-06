from rest_framework import serializers
from rest.models import Work

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
        