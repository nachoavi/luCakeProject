from django.db import models

# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ProductsInventory(models.Model):
    name = models.CharField(max_length=100,null=False)
    price = models.PositiveIntegerField(null=False)
    category = models.ForeignKey(CategoryProduct, on_delete=models.PROTECT)
    elabDate = models.DateField()
    expDate = models.DateField()
    stock = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return self.name
    

class ClientContacts(models.Model):
    name = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=100,null=False)
    rut = models.CharField(max_length=13,null=False)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name + " " + self.lastname
    
    
class Roles(models.TextChoices):
    ADMIN = 'Admin'
    NORMAL_USER = 'NormalUser'
    
class UserCollaborator(models.Model):
    name = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=100,null=False)
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=150,null=False)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.NORMAL_USER
    )
    
    def __str__(self):
        return self.username

    
class Sales(models.Model):
    product = models.ForeignKey(ProductsInventory, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(null=False)
    saleDate = models.DateTimeField(auto_now_add=True)
    subtotal = models.PositiveIntegerField(null=False)
    iva = models.PositiveBigIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
    seller = models.ForeignKey(UserCollaborator,on_delete=models.PROTECT)
    
    
class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
         
class Recipes(models.Model):
    title = models.CharField(max_length=50,null=False)
    ingredients = models.ManyToManyField(Ingredients)
    directions = models.TextField(null=False)
    
    def __str__(self):
        return self.title
    

class Suppliers(models.Model):
    name = models.CharField(max_length=60,null=False)
    email = models.EmailField(max_length=60,null=False)
    phone = models.CharField(max_length=20,null=True)
    rut = models.CharField(max_length=15,null=False)
    address = models.CharField(max_length=200,null=False)
    products = models.CharField(max_length=200,null=False)
    
    

