from django.shortcuts import render

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

def clientContacts(request):
    return render(request,'clientContacts/clientContactsTable.html')

def clientContactsForm(request):
    return render(request,'clientContacts/clientContactsForm.html')

def recipes(request):
    return render(request,'recipes/recipes.html')

def recipesForm(request):
    return render(request,'recipes/recipesForm.html')