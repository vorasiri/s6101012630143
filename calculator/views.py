from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Operation
def home(request):
    return render(request,'home.html')

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
        op_minus = request.POST['minus']
        op_multiply = request.POST['multiply']
        op_divide = request.POST['divide']
        result = 0
        if op_add:
            result = x + y
        elif op_minus:
            result = x - y
        elif op_multiply:
            result = x * y
        elif op_divide:
            result = x / y
        return HttpResponse(result)

