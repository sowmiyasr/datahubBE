from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import pipiline_sch
from pipeline_framework.models import pipe_fram
from rest_framework.views import APIView
from pipeline_framework.serializers import Pipeline_frameserializer
from rest_framework.response import Response
from rest_framework import status
from datahub_v3_app.models import pipiline_sch
import json
import requests
import json

class demo(APIView):
    # def get(self):
    #     if pipiline_sch.

    data=requests.get('http://34.73.32.172:8000/connection_det/').text

    string=data

    char_remov = ["[", "]"]
    for char in char_remov:

        string = string.replace(char, "")

    print(string)
 
    test_string = string
    json.dumps([string])
    res = json.loads(json.dumps([string]))

    print(type(res))

    url = 'http://34.73.32.172:8000/connection_det/'


    myobj = res

    print(type(myobj))

    x = requests.get(url, json = myobj)

    print(x.text)




# class pipeline_fram(APIView):
#     def get_user_by_pk(self, pk):
#         try:
#             return pipiline_sch.objects.filter.get(pk=pk)
#         except:
#             return Response({
#                 'error': 'does not exist'
#             }, status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk=None):

#         if pk:
#                 reg = self.get_user_by_pk(pk)
#                 serializer = Pipeline_frameserializer(reg)
#                 return Response([serializer.data])

#         else:
#                 reg = pipiline_sch.objects.all()
#                 serializer = Pipeline_frameserializer(reg, many=True)
#                 return Response(serializer.data)
