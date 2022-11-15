from dataclasses import fields
from rest_framework import serializers
from datahub_v3_app.models import pages


class pagedetserializer(serializers.ModelSerializer):

    class Meta:
        model= pages
        fields= ['id','page_name','module_name','page_url','start_date','end_date','is_active','created_by','created_on']