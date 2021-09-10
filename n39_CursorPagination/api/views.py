from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import CursorPagination
# Create your views here.

class MyCursorPagination(CursorPagination):
    page_size = 2
    # ordering = 'name'
    ordering = 'id'
    cursor_query_param = 'cu'

class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination