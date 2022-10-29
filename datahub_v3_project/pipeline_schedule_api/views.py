from django.shortcuts import render
from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import pipiline_sch
from rest_framework.views import APIView
from pipeline_schedule_api.serializers import pipelind_scheduleserializer
from rest_framework.response import Response

# Create your views here.
class pipeline_sch(APIView):
    def get_object(self, pk):
            try:
                return pipiline_sch.objects.get(pk=pk)
            except pipiline_sch.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = pipelind_scheduleserializer(data)
                return Response([serializer.data])

            else:
                data = pipiline_sch.objects.all()
                serializer = pipelind_scheduleserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = pipelind_scheduleserializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'connect_detail Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = pipiline_sch.objects.get(pk=pk)
        serializer = pipelind_scheduleserializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'conect_detail Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        conect_to_delete =  pipiline_sch.objects.get(pk=pk)

        conect_to_delete.delete()

        return Response({
            'message': 'connect_detail Deleted Successfully'
        })