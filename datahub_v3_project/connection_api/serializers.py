from rest_framework import serializers
from datahub_v3_app.models import conn

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = conn
        fields = "__all__"