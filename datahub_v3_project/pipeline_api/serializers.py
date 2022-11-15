from rest_framework import serializers
from datahub_v3_app.models import pipline_api
class pipline_Serializer(serializers.ModelSerializer):

    #description = serializers.SerializerMethodField()

    class Meta:
        model =  pipline_api
        fields = ['id','pipeline_name','email','Description','Start_date','End_date','is_active']