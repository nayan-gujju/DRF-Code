from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)

    def create(self, validated):
        return Student.objects.create(**validated)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    