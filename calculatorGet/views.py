from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from .models import Operation

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

def calGet(request):
    if request.method == "GET":
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        op = request.GET.get('op')
        result = 0
        if op=='add':
            result = add(x,y)
        elif op=='subtract':
            result = subtract(x,y)
        elif op=='multiply':
            result = multiply(x,y)
        elif op=='divide':
            result = divide(x,y)
        return render(request,'calculatorGet.html',{'result':result})