from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentInfo 
from enroll.models import User
from django.views.generic.base import TemplateView, RedirectView, View

# Create your views here.

#this is function for add ans show data

class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentInfo()      
        stud = User.objects.all()  
        context = {'stu':stud,'form':fm}
        return context

    def post(self, request):
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')


#this class for update
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentInfo(instance=pi) 
        return render(request, 'enroll/update.html', {'form':fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentInfo(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'enroll/update.html', {'form':fm})








#this class for delete
class UserDelete(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


