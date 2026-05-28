from rest_framework import serializers
from .models import EmissionRecord


class EmissionRecordSerializer(serializers.ModelSerializer):

    source_name = serializers.CharField(source='source.file_name')

    class Meta:
        model = EmissionRecord
        fields = '__all__'