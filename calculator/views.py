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
    # numCal = Operation()
    # numCal.x = ClearStrSpace(request.POST['x'])
    # numCal.y = ClearStrSpace(request.POST['y'])
    # numCal.op = ClearStrSpace(request.POST['op'])
    # numCal.save()

    if request.method == "POST":
        x = float(request.POST['x'])
        y = float(request.POST['y'])
        op_add = request.POST['add']
        # op_minus = request.POST['minus']
        # op_multiply = request.POST['multiply']
        # op_divide = request.POST['divide']
        result = 0
        if op_add:
            result = add(x,y)
        elif op_minus:
            result = subtract(x,y)
        elif op_multiply:
            result = multiply(x,y)
        elif op_divide:
            result = divide(x,y)
        # return HttpResponse(result)
        return render(request,'calculator.html',{'result':result})

