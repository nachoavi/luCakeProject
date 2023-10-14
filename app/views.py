from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# Create your views here.

def signin(request):
    return render(request,'signin.html')

def baseHTML(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def usersTable(request):
    return render(request,'users/usersTable.html')

def usersForm(request):
    return render(request,'users/usersForm.html')

def productsTable(request):
    return render(request,'products/productsTable.html')

def productsForm(request):
    return render(request,'products/productsForm.html')

def salesTable(request):
    return render(request,'sales/salesTable.html')

def sell(request):
    return render(request,'sales/sell.html')

def clientContacts(request):
    if request.method == 'GET':
        clientsList = ClientContacts.objects.all()
        return render(request,'clientContacts/clientContactsTable.html',{
            'clients':clientsList
        })

def clientContactsForm(request):
    if request.method == 'GET':
        return render(request,'clientContacts/clientContactsForm.html')
    else:
        newClient = ClientContacts.objects.create(
            name=request.POST['name'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            rut=request.POST['rut'],
            phone=request.POST['phone']
        )
        newClient.save()
        return redirect('clientContacts')


def recipes(request):
    return render(request,'recipes/recipes.html')

def recipesForm(request):
    return render(request,'recipes/recipesForm.html')