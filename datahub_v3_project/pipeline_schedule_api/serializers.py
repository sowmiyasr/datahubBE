from dataclasses import fields
from rest_framework import serializers
from datahub_v3_app.models import pipiline_sch


class pipelind_scheduleserializer(serializers.ModelSerializer):

    class Meta:
        model= pipiline_sch
        fields = '__all__'
        # fields=['pipeline_detail_id','pipeline_schedule_start_date','pipeline_schedule_end_date','pipeline_schedule_desc',
        #         'pipeline_schedule_run_imme','pipeline_status','pipeline_schedule_time']