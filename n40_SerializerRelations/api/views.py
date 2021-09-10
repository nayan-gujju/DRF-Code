from django.shortcuts import render
from .forms import SingerForm, SongForm
from .serializers import SingerSrializer, SongSerializer
from .models import Singer, Song
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSrializer

class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

def list(request):
    if request.method == 'POST':
        fm = SingerForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SingerForm()
    return render(request, 'api/home.html', {'form':fm})        

def songlist(request):
    if request.method == 'POST':
        song = SongForm(request.POST)
        if song.is_valid():
            song.save()
    else:
        song = SongForm()
    return render(request, 'api/song.html', {'song':song})        