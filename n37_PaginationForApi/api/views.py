from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.


# class MyPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'records'
#     max_page_size = 5

class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyPagination
