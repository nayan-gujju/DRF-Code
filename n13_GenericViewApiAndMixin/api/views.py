from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentList(ListModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class StudentRetrieve(RetrieveModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 

class StudentCreate(CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentUpdate(UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentUpdatePatch(UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentDelete(DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)