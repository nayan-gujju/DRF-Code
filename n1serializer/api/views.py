from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
# Create your views here.

#Model Object -Single Student Data -Finction Based View

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)

    return JsonResponse(serializer.data, safe=True)
    # return HttpResponse(json_data, content_type='application/json')

def studentlist(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)

    return JsonResponse(serializer.data, safe=False )
    # return HttpResponse(json_data, content_type='application/json')