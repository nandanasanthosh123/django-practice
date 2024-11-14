from django.shortcuts import render
from.models import*
# Create your views here.


def sample(request):
    return render(request,'task.html')