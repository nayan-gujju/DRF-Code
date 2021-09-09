from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import SearchFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [SearchFilter]
    search_fields = ['city']
    # search_fields = ['^name',]#this search start with character of name
    # search_fields = ['=name',]#search only exact word of name