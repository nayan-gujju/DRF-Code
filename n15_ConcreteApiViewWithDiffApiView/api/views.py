from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

# Concrete LIST API VIEW
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete RETRIEVE API VIEW
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete UPDATE API VIEW
class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete DESTROY API VIEW
class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete LIST_CREATE API VIEW
class StudentLCAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Concrete RETRIEVE_UPDATE API VIEW
class StudentRUAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete RETRIEVE_DEASTROY API VIEW
class StudentRDAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Concrete RETRIEVE_UPDATE_DESTROY API VIEW
class StudentRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



