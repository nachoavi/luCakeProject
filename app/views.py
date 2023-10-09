from django.shortcuts import render

# Create your views here.

def baseHTML(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def usersTable(request):
    return render(request,'users/usersTable.html')

def usersForm(request):
    return render(request,'users/usersForm.html')