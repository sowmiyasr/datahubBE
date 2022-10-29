from rest_framework import serializers
from datahub_v3_app.models import db_config


class db_configserializer(serializers.ModelSerializer):

    class Meta:
        model= db_config
        fields= ['id','config_name','desc','start_date','end_date','is_active']