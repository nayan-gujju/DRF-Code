from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer