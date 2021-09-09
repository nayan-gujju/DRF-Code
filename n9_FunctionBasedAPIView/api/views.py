from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

""" @api_view([])
def hello_world(request):
    return Response({'msg':'Hello World'}) """

""" @api_view(['GET'])
def hello_world(request):
    return Response({'msg':'Hello World'}) """

""" @api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        print('===========')
        print(request.data)
        return Response({'msg':'This is POST request'}) """

""" @api_view(['GET','POST'])
def hello_world(request):
    if request.method == "POST":
        print('===========')
        print(request.data)
        return Response({'msg':'This is POST request'})
    return Response({'msg':'This is GET method'}) """

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        print('++++++++++++')
        print(request.data)
        return Response({'msg':'This is GET method'})
    if request.method == "POST":
        print('===========')
        print(request.data)
        return Response({'msg':'This is POST request', 'data':request.data})
