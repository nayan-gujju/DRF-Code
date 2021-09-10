from django.forms import ModelForm
from .models import Singer,Song


class SingerForm(ModelForm):
    class Meta:
        model = Singer
        fields = '__all__'

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
