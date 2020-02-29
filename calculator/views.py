from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Operation

def home(request):
    return render(request,'home.html')
def calPost(request):
    return render(request,'calPost.html')
def calGet(request):
    return render(request,'calGet.html')
def about(request):
    return render(request,'about.html')

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

def cal(request):
    if request.method == "POST":
        x = float(request.POST['x'])
        y = float(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op=='add':
            result = add(x,y)
        elif op=='subtract':
            result = subtract(x,y)
        elif op=='multiply':
            result = multiply(x,y)
        elif op=='divide':
            result = divide(x,y)
        # return HttpResponse(result)
        return render(request,'calPost.html',{'result':result})

