from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from .serializers import StudentSerializer
from .models import Student
# Create your views here.


class StudentModelView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # permission_classes = [IsAdminUser]
   
    #if user is authenticatded then its perform all operation otherwise only read the api data  
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #same as django model permission 
    # permission_classes = [DjangoModelPermissions]


    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    permission_classes = [DjangoObjectPermissions]