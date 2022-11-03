from django.shortcuts import render
from role_detail_api.serializers import role_detail_serializer
from ast import Delete
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from django.http.response import Http404
from datahub_v3_app.models import role_detail_api
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class role_details_api(APIView):
    def get_object(self, pk):
            try:
                return role_detail_api.objects.get(pk=pk)
            except role_detail_api.DoesNotExist:
                raise Http404

                return Response(serializer.data)


    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = role_detail_serializer(data)
                return Response(serializer.data)


            else:
                data = role_detail_api.objects.all()
                serializer = role_detail_serializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = role_detail_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Role detail Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = role_detail_api.objects.get(pk=pk)
        serializer = role_detail_serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Role detail Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        conect_to_delete = role_detail_api.objects.get(pk=pk)

        conect_to_delete.delete()

        return Response({
            'message': 'Role detail Deleted Successfully'
        })