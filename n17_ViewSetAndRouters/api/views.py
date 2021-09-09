from functools import partial
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('*************List********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('*************List********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
    def create(self, request):
        print('*************Create********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created.."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        print('*************Update********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated"}, status=status.HTTP_100_CONTINUE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        print('*************Partical update********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partical Data Updated"}, status=status.HTTP_100_CONTINUE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        print('*************Destroy********')
        print('BaseName:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted.."}, status=status.HTTP_100_CONTINUE)