from django.shortcuts import render
from django.http import HttpResponse

def fnName2(request):
    return HttpResponse("HLO USER")
def fnName3(request):
    return render(request,'New.html')
def fnHome(req):
    return render(req,'Home.html')
def fnData(req):
    return render(req,'Data.html')  
def fnUser(req):
    return render(req,'User.html')            
# Create your views here.
