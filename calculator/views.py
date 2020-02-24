from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def cal(request):
    x = 0
    y = 0
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*"
        return x
