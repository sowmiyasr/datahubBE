from rest_framework import serializers
from datahub_v3_app.models import pipline_table
class pipline_Serializer(serializers.ModelSerializer):

    #description = serializers.SerializerMethodField()

    class Meta:
        model =  pipline_table
        fields = ['id','pipeline_name','Description','Start_date','End_date','is_active']