from django.shortcuts import render
from.models import*
# Create your views here.

def index(request):
    return render(request,'workspace.html')

def sign_view(request):
    return render(request, 'index.html')
