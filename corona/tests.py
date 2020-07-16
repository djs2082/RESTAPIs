from django.test import TestCase
import json
from rest_framework.test import APITestCase
from rest_framework import status


class TestCorona(APITestCase):
    def test_all(self):
        response=self.client.get('/corona/')
        parsed_json = (json.loads(response.content))
        ind_cases=parsed_json['India']['cases']
        maha_cases=parsed_json['Maharashtra']['state_cases']
        dist_cases=parsed_json['Maharashtra']['districts']['Nanded']['cases']
        self.assertTrue(int(ind_cases.replace(',','')) > 1 and int(maha_cases.replace(',','')) > 1 and int(dist_cases.replace(',','')) >1 and response.status_code == status.HTTP_200_OK)
        
    def test_state(self):
        response=self.client.get('/corona/maharashtra/')
        data=json.loads(response.content)
        maha_cases=data['Maharashtra']['state_cases']
        districts_length=len(data['Maharashtra']['districts'])
        nan_cases=data['Maharashtra']['districts']['Nanded']['cases']
        self.assertTrue(int(maha_cases.replace(',','')) > 1 and int(districts_length) == 36 and int(nan_cases.replace(',','')) > 1 and response.status_code == status.HTTP_200_OK)

    def test_dist(self):
        response=self.client.get('/corona/maharashtra/nanded/')
        data=json.loads(response.content)
        ind_cases=data['India']['cases']
        maha_cases=data['Maharashtra']['state_cases']
        dist_cases=data['Maharashtra']['districts']['Nanded']['cases']
        self.assertTrue(int(ind_cases.replace(',','')) > 1 and int(maha_cases.replace(',','')) > 1 and int(dist_cases.replace(',','')) > 1 and response.status_code == status.HTTP_200_OK)

class TestStudent(APITestCase):

    def test_all(self):
        response=self.client.get('/students/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

