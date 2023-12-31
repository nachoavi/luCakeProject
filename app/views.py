from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import *
import bcrypt
import json

# Create your views here.

def signin(request):
    user_auth = request.session.get("isAuthenticated")

    try:
        users = UserCollaborator.objects.get(username="admin")
    except:
        bytes = "admin".encode("utf-8")
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        admin = UserCollaborator(
        name='Admin',
        lastname='Admin',
        email="admin@gmail.com",
        username="admin",
        password=hash,
        role="Admin"
    )
        admin.save()


    if user_auth is None:
        request.session["isAuthenticated"] = False


    if request.session["isAuthenticated"]:
        return redirect("/")
    else:
        if request.method == "GET":
            return render(request,'signin.html')
        else:
            user_email = request.POST["user-email"]
            password = request.POST["password"]
            if user_email == "" or password == "":
                return render(request,'signin.html', {"void_credentials": "void_credentials"})
            get_user = UserCollaborator.objects.get(email=user_email)
            password_bytes = password.encode("utf-8")

            result = bcrypt.checkpw(password_bytes, get_user.password)
            if result:
                request.session["isAuthenticated"] = True
                request.session["username"] = get_user.username
                request.session["id_user"] = get_user.id
                request.session["role"] = get_user.role
                return redirect("/")
            
            else:
                return render(request,'signin.html', {"error": "error"})
        

def logout(request):
    request.session["isAuthenticated"] = False
    return redirect("/signin")


def baseHTML(request):
    return render(request,'base.html', {"username": request.session["username"]})

def home(request):
    user_auth = request.session.get("isAuthenticated")
    products = ProductsInventory.objects.all()

    if not user_auth:
        return redirect("/signin")
        
    else:
        low_stock = ""
        for data in products:
            if data.stock < 3:
                low_stock = data.name
        request.session["low_stock"] = low_stock


        return render(request,'home.html')

    

def usersTable(request):
    role = request.session.get("role")
    if role == "Admin":
        if request.method == 'GET':
            users = UserCollaborator.objects.all()
            
            return render(request,'users/usersTable.html',{'users':users})
    else:
        return redirect("/")

    

def createUser(request):
    admin = Roles.ADMIN
    normalUser = Roles.NORMAL_USER
    role = request.session.get("role")
    if role == "Admin": 
        if request.method == 'GET':       
            return render(request,'users/createUser.html',{'admin':admin, 'normalUser':normalUser})
        else:
            errorMesaggeUsername = 'El nombre de usuario que has ingresado no está disponible'
            errorMesaggeEmail = 'El email que has ingresado ya se encuentra registrado'
            users = UserCollaborator.objects.all()
            for user in users:
                if user.username == request.POST['username'] and user.email == request.POST['email']:
                    return render(request,'users/createUser.html',{'admin':admin, 'normalUser':normalUser,'errorUsername':errorMesaggeUsername,'errorEmail':errorMesaggeEmail})
                elif user.username == request.POST['username']:
                    return render(request,'users/createUser.html',{'admin':admin, 'normalUser':normalUser,'errorUsername':errorMesaggeUsername})
                elif user.email == request.POST['email']:
                    return render(request,'users/createUser.html',{'admin':admin, 'normalUser':normalUser,'errorEmail':errorMesaggeEmail})
                
            password = str(request.POST['password'])
            bytes = password.encode("utf-8")
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            newUser = UserCollaborator.objects.create(
                name=request.POST['name'],
                lastname=request.POST['lastname'],
                email=request.POST['email'],
                username=request.POST['username'],
                password=hash,
                role = request.POST['role']
            )
            newUser.save()
            return redirect('usersTable')
    else:
        return redirect("/")

def updateUser(request,id):
    user = UserCollaborator.objects.get(id=id)
    admin = Roles.ADMIN
    normalUser = Roles.NORMAL_USER
    role = request.session.get("role")
    if role == "Admin":
        if request.method == 'POST':
            user.name = request.POST.get('name')
            user.lastname = request.POST.get('lastname')
            user.email = request.POST.get('email')
            user.username = request.POST.get('username')
            password = request.POST.get('password')
            user.role = request.POST.get('role')
            bytes = password.encode("utf-8")
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            user.password = hash
            user.save()
            return redirect('usersTable')
        return render(request,'users/updateUser.html',{'user':user,'admin':admin,'normalUser':normalUser})
    else:
        return redirect("/")

def deleteUser(request,id):
    role = request.session.get("role")
    user = UserCollaborator.objects.get(id=id)
    if role == "Admin":
        user.delete()
        return redirect('usersTable')
    else:
        return redirect("/")
    
def categories(request):
    categories_data = CategoryProduct.objects.all()
    return render(request, "categories/categories.html", {"categories": categories_data})

def add_categorie(request):
    if request.method == "GET":
        return render(request, "categories/categories_form.html")
    else:
        categorie_name = request.POST.get("categorie_name")
        if not categorie_name:
            return render(request, "categories/categories_form.html", {"error": "No has agregado ninguna categoría"})
        else:
            new_categorie = CategoryProduct(name=categorie_name)
            new_categorie.save()
        return redirect("/categories")

def productsTable(request):
    role = request.session.get("role")
    if role == "Admin" or role == "NormalUser":
        if request.method == 'GET':
            products = ProductsInventory.objects.all()
            return render(request,'products/productsTable.html',{'products':products})
    else:
        return redirect("/")

def createProducts(request):
    role = request.session.get("role")
    if role == "Admin" or role == "NormalUser":
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
    else:
        return redirect("/")

def updateProduct(request,id):
    role = request.session.get("role")
    if role == "Admin" or role == "NormalUser":
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
    else:
        return redirect("/")

def deleteProducts(request,id):
    product = get_object_or_404(ProductsInventory, id=id)
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        product.delete()
        return redirect('productsTable')
    
    else:
        return redirect("/")


def salesTable(request):
    role = request.session.get("role")
    sold_products = Sales.objects.all()
    if role == "Admin" or role == "NormalUser":
        return render(request,'sales/salesTable.html', {"sales": sold_products})
    else:
        return redirect("/")

def sell(request):
    role = request.session.get("role")
    products_data = ProductsInventory.objects.all()
    if role == "Admin" or role == "NormalUser":
        if request.method == "GET":
            return render(request,'sales/sell.html', {"products": products_data})
        else:
            try:

                for key, value in request.POST.items():
                    if key.startswith('product_selected_'):
                        product_id = value
                        quantity_key = f'product_quantity_{key.split("_")[-1]}'
                        product_quantity = int(request.POST.get(quantity_key, 0))
                        product = ProductsInventory.objects.get(id=product_id)
                        if product.stock <= 0:
                            errorStock = 'No hay stock del producto'
                            return render(request,'sales/sell.html', {"products": products_data,'errorStock': errorStock})
                        if product_quantity > product.stock:
                            errorStock = 'No hay suficiente stock para vender esta cantidad'
                            return render(request,'sales/sell.html', {"products": products_data,'errorStock': errorStock})
                        
                        product.stock -= product_quantity
                        product.save()

            
                        product_subtotal = product.price * product_quantity
                        product_total = product.price * product_quantity + (product.price * 0.19)

        
                        sale = Sales(
                            product=product,
                            amount=product_quantity,
                            saleDate=timezone.now(),
                            subtotal=product_subtotal,
                            iva=19,
                            total=product_total,
                            seller=UserCollaborator(id=request.session["id_user"])
                        )
                        sale.save()

        
        
                return redirect("/sales")
            except ValueError:
                return render(request,'sales/sell.html', {"products": products_data})
    else:
        return redirect("/")

def clientContacts(request):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        if request.method == 'GET':
            clientsList = ClientContacts.objects.all()
            return render(request,'clientContacts/clientContactsTable.html',{
                'clients':clientsList
            })
    else:
        return redirect("/")

def createClientContacts(request):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
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
    else:
        return redirect("/")
    
def updateClientContacts(request,id):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
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
    else:
        return redirect("/")
    
def deleteClientContacts(request,id):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        client = ClientContacts.objects.get(id=id)
        client.delete()
        return redirect("clientContacts")
    else:
        return redirect("/")

def recipes(request):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        recipes_data = Recipes.objects.all()
        return render(request,'recipes/recipes.html', {"recipes": recipes_data})
    else:
        return redirect("/")
    
def recipes_see(request, id_recipe):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        recipe_data = Recipes.objects.get(id=id_recipe)
        ingredients_data = recipe_data.ingredients.split(", ")
        print(ingredients_data)
        return render(request, "recipes/recipeContent.html", {"recipe": recipe_data, "ingredients": ingredients_data})
    else:
        return redirect("/")
    
def recipes_delete(request, id_recipe):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        recipe = Recipes.objects.get(id=id_recipe)
        recipe.delete()
        return redirect("/recipes")
    else:
        return redirect("/")
    
def recipesForm(request):
    role = request.session.get("role")
    
    if role == "Admin" or role == "NormalUser":
        if request.method == "GET":
            return render(request,'recipes/recipesForm.html')
        else:
            recipe_name = request.POST["recipe_name"]
            recipe_ingredients = request.POST["recipe_ingredients"]
            recipe_preparation = request.POST["recipe_preparation"]
            recipe_description = request.POST["recipe_description"]
            recipe_image = request.POST["url_img"]
            new_recipe = Recipes(title=recipe_name, description=recipe_description, url_img=recipe_image, ingredients=recipe_ingredients, directions=recipe_preparation)
            new_recipe.save()
            return redirect("/recipes")
    else:
        return redirect("/")

def suppliersTable(request):
    role = request.session.get("role")
    
    if role == "Admin":
        if request.method == 'GET':
            suppliersList = Suppliers.objects.all()
            return render(request,'suppliers/suppliersTable.html',{
                'suppliers':suppliersList
            })
    else:
        return redirect("/")

def createSuppliers(request):
    role = request.session.get("role")
    
    if role == "Admin":
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
    else:
        return redirect("/")
    
def updateSuppliers(request,id):
    role = request.session.get("role")
    
    if role == "Admin":
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
    else:
        return redirect("/")
   
    
def deleteSuppliers(request,id):
    role = request.session.get("role")
    
    if role == "Admin":
        supplier = Suppliers.objects.get(id=id)
        supplier.delete()
        return redirect("suppliersTable")
    else:
        return redirect("/")

def costOfSales(request):
    role = request.session.get("role")
    if role == "Admin":
        if request.method == 'GET':
            return render(request,'salesPriceCalculator/form.html')
        else:
            raw_material = float(request.POST["raw_material"])
            labour = float(request.POST["labour"])
            indirect_costs = float(request.POST["indirect_costs"])
            indirect_expenses = float(request.POST["indirect_expenses"])
            utility_margin = float(request.POST["utility_margin"]) / 100

            total_cost = sum([raw_material, labour, indirect_costs, indirect_expenses])
            print(total_cost)
            print(utility_margin)
            price_sale = (total_cost / (1 - utility_margin))

            return render(request,'salesPriceCalculator/form.html', {"price_sale": price_sale})


    else:
        return redirect("/")