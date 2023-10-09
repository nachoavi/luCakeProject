from django.shortcuts import render

# Create your views here.

def baseHTML(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')