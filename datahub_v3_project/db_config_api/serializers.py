from rest_framework import serializers
from datahub_v3_app.models import db_conf


class db_configserializer(serializers.ModelSerializer):

    class Meta:
        model= db_conf
        fields= ['id','config_name','desc','source_connection_name','target_connection_name','start_date','end_date','is_active']