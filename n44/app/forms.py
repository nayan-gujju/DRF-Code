from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'roll', 'city')

class UserForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}