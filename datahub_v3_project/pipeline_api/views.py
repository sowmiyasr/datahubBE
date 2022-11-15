from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import pipline_api
from rest_framework.views import APIView
from pipeline_api.serializers import pipline_Serializer
from rest_framework.response import Response
from rest_framework import status

class pipeline(APIView):
    def get_user_by_pk(self, pk):
        try:
            return pipline_api.objects.get(pk=pk)
        except:
            return Response({
                'error': 'does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):

        if pk:
                reg = self.get_user_by_pk(pk)
                serializer = pipline_Serializer(reg)
                return Response([serializer.data])

        else:
                reg = pipline_api.objects.all()
                serializer = pipline_Serializer(reg, many=True)
                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = pipline_Serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = pipline_api.objects.get(pk=pk)
        serializer = pipline_Serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        todo_to_delete =  pipline_api.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Deleted Successfully'
        })

