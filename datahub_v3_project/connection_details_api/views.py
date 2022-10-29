# Create your views here.
from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import con_details
from rest_framework.views import APIView
from connection_details_api.serializers import connection_details_keypairsserializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class detail(APIView):
    def get_object(self, pk):
            try:
                return con_details.objects.get(pk=pk)
            except con_details.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = connection_details_keypairsserializer(data)
                return Response([serializer.data])

            else:
                data = con_details.objects.all()
                serializer = connection_details_keypairsserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        try:

            # import pdb
            # pdb.set_trace()
            connection_name_data = request.data.get('connection_name', None)
            connection_detail_data = request.data.get('connection_detail', None)
            conn_pd_id_data = request.data.get('conn_pd_id', None)
            con_pram_data = request.data.get('con_pram', [])
            # key_pram_data = request.data.get('key_pram', [])
            start_date_data = request.data.get('start_date', None)
            end_date_data = request.data.get('end_date', None)
            last_modified_by_data = request.data.get('last_modified_by', None)
            last_modified_on_data = request.data.get('last_modified_on', None)
            created_on_data = request.data.get('created_on', None)
            created_by_data = request.data.get('created_by', None)
            is_active_data = request.data.get('is_active', None)
            # import pdb
            # pdb.set_trace()
            cnt=0
            for con_pram_loop in con_pram_data:

                request_data={
                    "connection_name":connection_name_data,
                    "connection_detail":connection_detail_data,
                    "conn_pd_id":conn_pd_id_data,
                    "key_pram":con_pram_loop['key'],
                    "value_pram":con_pram_loop['value'],
                    "start_date":start_date_data,
                    "end_date":end_date_data,
                    "last_modified_by":last_modified_by_data,
                    "last_modified_on":last_modified_on_data,
                    "created_on":created_on_data,
                    "created_by":created_by_data,
                    "is_active":is_active_data,

                }
                # import pdb
                # pdb.set_trace()
                serializer = connection_details_keypairsserializer(data=request_data)
                if serializer.is_valid():
                    serializer.save()
                cnt=cnt+1



            return Response(cnt, status=200)
        except:
            return Response('error', status=400)


    def put(self, request, pk=None, format=None):
        conn_to_update = con_details.objects.get(pk=pk)
        serializer = connection_details_keypairsserializer(instance=conn_to_update,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'conect_detail Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        conect_to_delete =  con_details.objects.get(pk=pk)
        conect_to_delete.delete()
        return Response({
            'message': 'connect_detail Deleted Successfully'
        })