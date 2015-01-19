from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def add(request):

    return HttpResponse("eee")

def update(request):
    return ""

def login(request):
    return ""

def delete(request):
    return render(request,"",{})

def list(request):
    return render(request,"",{})

def query(request):
    return render(request,"",{})