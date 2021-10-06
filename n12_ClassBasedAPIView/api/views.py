from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
class StudentApi(APIView):

    def get(self, request, pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk , format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated...'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk ,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partical Data Updated...'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted...'}, status=status.HTTP_100_CONTINUE)
