from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4 #this show only 4 data in one page
    limit_query_param = 'mylimit' #this set name in url by default name is limit
    offset_query_param  = 'off' # this set name in url by default name is offset
    max_limit = 6

class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination
   