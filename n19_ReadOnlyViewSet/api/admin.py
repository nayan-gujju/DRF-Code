from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        list_display = ['id', 'name','roll', 'city']