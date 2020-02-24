from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def cal(request):
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x / y
    return result
