from django.shortcuts import redirect, render
from app.forms import StudentForm, UserForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class Home(TemplateView):
    template_name = 'app/home.html'

class Index(TemplateView):
    template_name = 'app/index.html'

class Index1(TemplateView):
    template_name = 'app/index1.html'

@login_required
def student_registration(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('student_reg')
    else:
        fm = StudentForm()
    return render(request,'app/registration.html', {'form':fm})


def user_registration(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('user_reg')
    else:
        fm = UserForm()
    return render(request,'app/registration.html', {'form':fm})