from django.shortcuts import render
from django.http import HttpResponse

def fnUser(req):
    return render(req,'User.html')
def fnDetails(req):
    return render(req,'Details.html')
# Create your views here.
