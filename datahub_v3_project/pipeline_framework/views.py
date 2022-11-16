from django.shortcuts import render
from rest_framework.views import APIView
#from.models import pipe_line
#from .serializers import pipe_lineserializer
from django.http.response import Http404
from urllib import response
from rest_framework.response import Response
import requests
from pipeline_framework import tests
import subprocess
import datetime
from datahub_v3_app.models import pipeline
from pipeline_api.serializers import pipline_Serializer

class pipe_framework(APIView):
    subprocess.call(['python','tests.py'])
    # update = pipline_table.objects.get(pipline_table)
    # def put(self, request, pk=None, format=None):
    #     conn_to_update = pipline_table.objects.get(pk=pk)
    #     serializer = pipline_Serializer(instance=conn_to_update,data=request.data, partial=True)

    #     serializer.is_valid(raise_exception=True)

    #     serializer.save()

    #     response = Response()

    #     response.data = {
    #             'message': ' Updated Successfully',
    #             'data': serializer.data
    #         }

    #     return response
    def hpot(request):
        # update = pipline_table.objects.get(id='id')
        url=requests.get('http://34.73.32.172:8000/schedule_dep/')
        return url.json()
    def get(self,request):
        data=self.hpot()
        new_data=[]
        i=12
        for datas in data:
            temp_dict={}
            #import pdb
            #pdb.set_trace()
            temp_dict['id']=datas['id']
            new_data.append(temp_dict)
            if i==temp_dict['id']:
                return Response('valid data')
            else:
                return Response('not valid')
        return Response(new_data)
