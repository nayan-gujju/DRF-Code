from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .serializer import StudentSerializer, RegisterSerializer
from app.models import Student
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here. 

class StudentList(APIView): 
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/api.html'    
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'datas': queryset})

class StudentDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(profile)
        return Response({"serializer":serializer, 'profile':profile})
    
    def post(self, request, pk):
        profile = get_object_or_404(Student, pk=pk)
        print("profile ",profile)
        serializer = StudentSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('student_api')

class StudentDelete(APIView):    
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk):
        stu = get_object_or_404(Student, pk=pk)
        stu.delete()    
        return redirect('student_api')


class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/userapi.html'
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        queryset = User.objects.all()
        return Response({'datas': queryset})


class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = RegisterSerializer(profile)
        return Response({"serializer":serializer, 'profile':profile})
    
    def post(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        print("profile ",profile)
        serializer = RegisterSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('user_api')

class UserDelete(APIView):    
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk):
        stu = get_object_or_404(User, pk=pk)
        stu.delete()    
        return redirect('user_api')