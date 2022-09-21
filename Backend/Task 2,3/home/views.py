from ast import main
import re
from django.shortcuts import render,HttpResponse
from . import Task_1
import requests
import json

def index(request):
    return render(request,'index.html') 
    
def task2(request,a,b):
    a=int(a)
    b=int(b)
    
    
    return HttpResponse(str(Task_1.madmax(a,b)))
   
def task3(request):
    
    response=requests.get('https://api.covid19api.com/countries').json()
    
   
    if 'your_name' in request.GET:
     your_name = request.GET['your_name']
    else:
        # to avoid not null constraint failed error
     your_name = False

    yolo=False
    for i in response:
        if i['Country']==your_name:
            
            Context={
                "Country":i['Country'],
                "Slug":i['Slug'],
                "ISO2":i['ISO2'],
            }
            yolo=True
           
        
    if yolo==True:        
     return render(request,"index.html",Context)
    else:
        return render(request,'sub.html')
        
