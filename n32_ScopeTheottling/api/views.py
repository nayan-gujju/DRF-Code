from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.

# Concrete LIST API VIEW
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewset'

# Concrete Create Api VIEW
class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'viewset'


# Concrete RETRIEVE API VIEW
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewset'

# Concrete UPDATE API VIEW
class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'

# Concrete DESTROY API VIEW
class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'

# # Concrete LIST_CREATE API VIEW
# class StudentLCAPIView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# # Concrete RETRIEVE_UPDATE API VIEW
# class StudentRUAPIView(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # Concrete RETRIEVE_DEASTROY API VIEW
# class StudentRDAPIView(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # Concrete RETRIEVE_UPDATE_DESTROY API VIEW
# class StudentRUDAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



