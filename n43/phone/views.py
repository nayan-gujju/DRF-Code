from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'phone/home.html'

# def home(request):
#     return render(request, 'phone/home.html')

def registration(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm()
    return render(request,'phone/registration.html', {'form':fm})

class StudentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'phone/api.html'

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'datas': queryset})