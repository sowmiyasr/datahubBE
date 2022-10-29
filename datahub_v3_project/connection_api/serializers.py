from rest_framework import serializers
from datahub_v3_app.models import Conn

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conn
        fields = "__all__"