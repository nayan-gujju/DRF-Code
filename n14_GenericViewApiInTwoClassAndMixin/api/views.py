from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class LCStudent(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RUDStudent(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



   