#  admin_username=maitreya    
#  admin_password=maitreya 

# .order_by
# values_list
from ast import main
import http
from typing import Counter
from unicodedata import name
from winreg import QueryInfoKey
from django.shortcuts import render,HttpResponse
from home.models import ApiVal
import requests
from django.db.models import F
# from django.shortcuts import render
def index(request):
    return HttpResponse("hi")

def forms(request):
 
    response=requests.get('https://api.covid19api.com/countries').json()
    
   
    if 'api' in request.POST:
     api = request.POST['api']
    else:
     api = False
    print(api)
    for i in response:
        if api==i['Country']:
            
            print(api)       
            if request.method=="POST":
               apicountry=request.POST.get('api')
               apiiso2=i['ISO2']
               apislug=i['Slug']
               counter=0
               print(i['Slug'])
               forms=ApiVal(apicountry=apicountry,apiiso2=apiiso2,apislug=apislug,counter=counter)
               forms.save()
               print("done")
               break
    return render(request,'forms.html')

def query(request):
    if 'query' in request.GET:
     query = request.GET['query']
    else:
     query = False
    ApiVal.objects.filter(apicountry=query).update(counter=F('counter') + 1)
    
    Context={
        "yay":list(ApiVal.objects.filter(apicountry=query).values_list('apicountry','counter')) 
    }

    print("done")
    return render(request,'query.html',Context)

def retrieve(request):
    Context={
    "first":list(ApiVal.objects.all().order_by('-counter')[0:1].values_list('apicountry','counter','apislug','apiiso2')),
    "second":list(ApiVal.objects.all().order_by('-counter')[1:2].values_list('apicountry','counter','apislug','apiiso2')),
    "third":list(ApiVal.objects.all().order_by('-counter')[2:3].values_list('apicountry','counter','apislug','apiiso2'))
    
    }
    return render(request,'retrieve.html',Context)