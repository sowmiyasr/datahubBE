from django.db import models

from django.db import models
from datahub_v3_app.models import pipiline_sch,pipline_det
# Create your models here.

class pipe_fram(models.Model):
    pipe_id = models.ForeignKey(pipiline_sch, primary_key=True,unique=True ,on_delete=models.CASCADE, blank=True, null=False,related_name='pipe_id')
    pipe_det_id = models.ForeignKey(pipline_det,unique=True , on_delete=models.CASCADE, blank=True, null=True,related_name='pipe_det_id')
    # pipe_status = models.ForeignKey(pipiline_sch, on_delete=models.CASCADE, blank=True, null=True,related_name='pipe_sts')

    class Meta:

     db_table = "pipeline_frame"
