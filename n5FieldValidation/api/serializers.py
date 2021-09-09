from rest_framework import serializers
from .models import Student

#valiatons
def start_with_n(value):
    if value[0].lower() != 'n':
        raise serializers.ValidationError('Name must be start with N')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_n])
    roll = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)

    def create(self, validated):
        return Student.objects.create(**validated)

    #Field Validation
    def validate_roll(self, value):
        if value >= 150:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #Object Validation
    def validate(self, data):
        nm = data.get('name')
        em = data.get('email')

        if nm.lower == 'nayan' and em.lower == 'nayan@gmail.com':
            raise serializers.ValidationError('Email Must Be')
        return data

