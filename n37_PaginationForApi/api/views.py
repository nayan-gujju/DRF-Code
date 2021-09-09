from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class MyPagination(PageNumberPagination):
    page_size = 3
    #page_query_param is show in url by deafult is page
    page_query_param = 'p'
    #page_size_query_param is number of  data for one page
    page_size_query_param = 'data'
    # max_page_size = 5
    #this for last page
    
    last_page_strings = 'end'

class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination
