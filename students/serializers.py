from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.Serializer):
    merit=serializers.IntegerField()
    score=serializers.IntegerField()
    enrollment = serializers.CharField(max_length=30)
    name=serializers.CharField(max_length=50)
    branch=serializers.CharField(max_length=50)
    year=serializers.CharField(max_length=20)
    gender=serializers.CharField(max_length=1)
    categeory=serializers.CharField(max_length=10)
    seattype=serializers.CharField(max_length=20)
    mobile_number=serializers.CharField(max_length=10)
    department=serializers.CharField(max_length=50)
    registeration_number=serializers.CharField(max_length=12)
    email_id=serializers.EmailField(max_length=50)


    def create(self,validated_data):
       return students.objects.create(**validated_data)


    def __str__(self):
        return self.email_id