from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    def start_with_n(value):
        if value[0].lower() != 'n':
            raise  serializers.ValidationError('Name must be start with N')
        return value
    
    name = serializers.CharField(validators=[start_with_n])
    
    class Meta:
        model = Student
        fields = ['id','name','roll' ,'email']
        
    def validate_roll(self, value):
        if value >=150:
            raise  serializers.ValidationError('Seat Full')
        return value


    def validate(self, data):
        nm = data.get('name')
        em = data.get('email')

        if nm.lower() == 'nayan' and em.lower() == 'nayan@gmail.com':
            raise  serializers.ValidationError('Email must be')
        return data

