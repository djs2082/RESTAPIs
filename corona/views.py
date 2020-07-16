from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import re
from bs4 import BeautifulSoup
import json
# Create your views here.

class Corona_API(APIView):
    def get(self,request,user_state=None,user_district=None):
        if user_state is not None:
            user_state=user_state.replace(' ','_')
            user_state=user_state.replace('-','_')
        url="https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html"
        response=requests.get(url)
        data=response.text
        soup=BeautifulSoup(data,'html.parser')
        states=soup.find_all('tr',{'class':'corona-state'})
        output=dict()
        country=soup.find_all('tr',{'id':'All'})
        country_name=country[0].find_all('td')[0].get_text()
        country_cases=country[0].find_all('td')[1].get_text()
        country_cases=country_cases.split(' ')
        country_cases=country_cases[0]

        country_deaths=country[0].find_all('td')[2].get_text()
        country_deaths=country_deaths.split(' ')
        country_deaths=country_deaths[0]

        country_recovered=country[0].find_all('td')[3].get_text()
        country_recovered=country_recovered.split(' ')
        country_recovered=country_recovered[0]   

        country_dict={}
        country_dict['cases']  = country_cases    
        country_dict['deaths']  = country_deaths          
        country_dict['recovered']  = country_recovered

        output[country_name]=country_dict           


        for state in states:
            state_name=state.find_all('td')[0].get_text()
            state_name=state_name.replace('-','_')
            state_name=state_name.replace(' ','_')
            print(state_name)
            if user_state is not None:
                if(state_name.lower() != user_state.lower()):
                     continue  
            districts=soup.find_all('tr',id=re.compile(r'tr{}'.format(state_name)))
            state_dict={}

            state_cases=state.find_all('td')[1].get_text()
            state_cases=state_cases.split(' ')
            state_cases=state_cases[0]

            state_deaths=state.find_all('td')[2].get_text()
            state_deaths=state_deaths.split(' ')
            state_deaths=state_deaths[0]

            state_recovered=state.find_all('td')[3].get_text()
            state_recovered=state_recovered.split(' ')
            state_recovered=state_recovered[0]         


            state_dict['state_name']=state_name
            state_dict['state_cases']=state_cases
            state_dict['state_deaths']=state_deaths
            state_dict['state_recovered']=state_recovered

            districts_dict={}
            for district in districts:
                district_name=district.find_all('td')[0].get_text()
                if user_district is not None:
                    if(district_name.lower()!=user_district.lower()):
                        continue
                    
                        
                temp_dict={}
                cases=district.find_all('td')[1].get_text()
                cases=cases.split(' ')
                temp_dict['cases']=cases[0]
                try:
                    color=district.find_all('td')[2]['style']
                except:
                    pass
                color=color[6:]
                color=color[:-1] 
                temp_dict['color']=color
                districts_dict[district_name]=temp_dict
            state_dict['districts']=districts_dict 
            output[state_name]=state_dict
        return(Response(output))



   

