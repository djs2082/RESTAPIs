from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import StudentsSerializer
from .models import Students
from rest_framework.response import Response
import json
# Create your views here.


class Students_API(APIView):

    def get(self, request, reg_no=None):
        if reg_no is not None:
            reg_no = reg_no.upper()
            queryset = get_object_or_404(Students.objects.all(), registeration_number=reg_no)
            serialized = StudentsSerializer(queryset)
        else:
            queryset = Students.objects.all()
            serialized = StudentsSerializer(queryset, many=True)
        return Response(serialized.data)

    def post(self, request):
        data={}
        data['merit'] = request.data.get('merit')
        data['score'] = request.data.get('score')
        data['enrollment'] = request.data.get('enrollment')
        data['name'] = request.data.get('name')
        data['branch'] = request.data.get('branch')
        data['year'] = request.data.get('year')
        data['gender'] = request.data.get('gender')
        data['categeory'] = request.data.get('categeory')
        data['seattype'] = request.data.get('seattype')
        data['mobile_number'] = request.data.get('mobile_number')
        data['department'] = request.data.get('department')
        data['registeration_number'] = request.data.get('registeration_number')
        data['email_id'] = request.data.get('email_id')
        print(data)
        user_data=json.dumps(data)
        serializer=StudentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved=serializer.save()

        print(user_data)
        return Response({"success":"student {}".format(saved)})





        # {
        # "merit": 200,
        # "score" : 190,
        # "enrollment" :  "en164444",
        # "name" : "dilip joshi",
        # "branch" : "cse",
        # "year" : "sy cse",
        # "gender" : "M",
        # "categeory" : "open",
        # "seattype" : "open",
        # "mobile_number" :  "8975427620",
        # "department" : "cse",
        # "registeration_number" : "2017bcs042",
        # "email_id" : "djs@gmail.com"
        # }