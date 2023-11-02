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
    if request.method == 'GET':
        users = UserCollaborator.objects.all()
        
        return render(request,'users/usersTable.html',{'users':users})

def createUser(request):
    admin = Roles.ADMIN
    normalUser = Roles.NORMAL_USER
    if request.method == 'GET':       
        return render(request,'users/createUser.html',{'admin':admin, 'normalUser':normalUser})
    else:
        newUser = UserCollaborator.objects.create(
            name=request.POST['name'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
            role = request.POST['role']
        )
        newUser.save()
        return redirect('usersTable')

def updateUser(request,id):
    user = UserCollaborator.objects.get(id=id)
    admin = Roles.ADMIN
    normalUser = Roles.NORMAL_USER
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.lastname = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.role = request.POST.get('role')
        user.save()
        return redirect('usersTable')
    return render(request,'users/updateUser.html',{'user':user,'admin':admin,'normalUser':normalUser})

def deleteUser(request,id):
    user = UserCollaborator.objects.get(id=id)
    user.delete()
    return redirect('usersTable')
    
def productsTable(request):
    if request.method == 'GET':
        products = ProductsInventory.objects.all()
        return render(request,'products/productsTable.html',{'products':products})

def createProducts(request):
    if request.method == 'GET': 
        categorys = CategoryProduct.objects.all()      
        return render(request,'products/createProducts.html',{'categorys':categorys})
    else:
        categoryID = CategoryProduct.objects.get(id=request.POST.get('category'))
        newProduct = ProductsInventory.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            category=categoryID,
            elabDate=request.POST['elabDate'],
            expDate=request.POST['expDate'],
            stock = request.POST['stock']
        )
        newProduct.save()
        return redirect('productsTable')

def updateProduct(request,id):
    product = ProductsInventory.objects.get(id=id)
    categorys = CategoryProduct.objects.all()  
    if request.method == 'POST':
        categoryID = CategoryProduct.objects.get(id=request.POST.get('category'))
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.category = categoryID
        product.elabDate = request.POST.get('elabDate')
        product.expDate = request.POST.get('expDate')
        product.stock = request.POST.get('stock')
        product.save()
        return redirect('productsTable')
    return render(request,'products/updateProducts.html',{'product':product,'categorys':categorys})

def deleteProducts(request,id):
    product = get_object_or_404(ProductsInventory, id=id)
    product.delete()
    return redirect('productsTable')



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

def createClientContacts(request):
    if request.method == 'GET':
        return render(request,'clientContacts/createClientContacts.html')
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
    
def updateClientContacts(request,id):
    client = ClientContacts.objects.get(id=id)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.lastname = request.POST.get('lastname')
        client.email = request.POST.get('email')
        client.rut = request.POST.get('rut')
        client.phone = request.POST.get('phone')
        client.save()
        return redirect('clientContacts')
    
    return render(request,'clientContacts/clientUpdate.html',{'client':client})
   
    
def deleteClientContacts(request,id):
    client = ClientContacts.objects.get(id=id)
    client.delete()
    return redirect("clientContacts")

def recipes(request):
    return render(request,'recipes/recipes.html')

def recipesForm(request):
    return render(request,'recipes/recipesForm.html')


def suppliersTable(request):
    if request.method == 'GET':
        suppliersList = Suppliers.objects.all()
        return render(request,'suppliers/suppliersTable.html',{
            'suppliers':suppliersList
        })

def createSuppliers(request):
    if request.method == 'GET':
        return render(request,'suppliers/createSuppliers.html')
    else:
        newSupplier = Suppliers.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            rut=request.POST['rut'],
            address=request.POST['address'],
            products=request.POST['products'])
        newSupplier.save()
        return redirect('suppliersTable')
    
def updateSuppliers(request,id):
    supplier = Suppliers.objects.get(id=id) 
    if request.method == 'POST':
        supplier.name = request.POST.get('name')
        supplier.email = request.POST.get('email')
        supplier.phone = request.POST.get('phone')
        supplier.rut = request.POST.get('rut')
        supplier.address = request.POST.get('address')
        supplier.products = request.POST.get('products')
        supplier.save()
        return redirect('suppliersTable')
    
    return render(request,'suppliers/suppliersUpdate.html',{'supplier':supplier})
   
    
def deleteSuppliers(request,id):
    supplier = Suppliers.objects.get(id=id)
    supplier.delete()
    return redirect("suppliersTable")