from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from .models import Operation

def home(request):
    return render(request,'home.html')
def calculatorPost(request):
    return render(request,'calculatorPost.html')
def calculatorGet(request):
    return render(request,'calculatorGet.html')
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

def calPost(request):
    if request.method == "POST":
        x = float(request.POST.get('x'))
        y = float(request.POST.get('y'))
        op = request.POST.get('op')
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
        return render(request,'calculatorPost.html',{'result':result})

