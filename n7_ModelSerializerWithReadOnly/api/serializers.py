from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        # fields = ['id','name','roll' ,'email']
        fields = '__all__'
        # read_only_fields = ['name', 'email'] 
        extra_kwargs = {'name':{'read_only':True},
            'email':{'read_only':True},
            }
    

    