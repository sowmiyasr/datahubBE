from rest_framework import serializers
from pipeline_framework.models import pipe_fram


class Pipeline_frameserializer(serializers.ModelSerializer):

    class Meta:
        model= pipe_fram
        fields = '__all__'