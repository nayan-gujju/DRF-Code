from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer