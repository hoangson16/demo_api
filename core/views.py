from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BaiVietSerializer
from .models import BaiViet


class TestView(APIView):
    
    def get(self, request):
        data = {
            'name': 'Son',
            'age': 27,
        }
        return Response(data)

class TestView2(APIView):

    def get(self, request):
        data = [
            {
                'name': 'Son',
                'age': 27,
            },
            {
               'name': 'Dat',
               'age': 27,
            },
        ]
        return Response(data)

class BaiVietViews(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        danh_sach_bai_viet = BaiViet.objects.all()
        serializer = BaiVietSerializer(danh_sach_bai_viet, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BaiVietSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BaiVietDetail(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        bai_viet = BaiViet.objects.get(pk=pk)
        serializer = BaiVietSerializer(bai_viet)
        return Response(serializer.data)

    def put(self, request, pk): 
        bai_viet = BaiViet.objects.get(pk=pk)
        serializer = BaiVietSerializer(bai_viet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        bai_viet = BaiViet.objects.get(pk=pk)
        bai_viet.delete()
        return Response({'message': 'Da xoa bai viet'})
