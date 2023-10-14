from django.db import models

# Create your models here.
class ProductsInventory(models.Model):
    name = models.CharField(max_length=100,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=3,null=False)
    stock = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return self.name
    

class ClientContacts(models.Model):
    name = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=100,null=False)
    rut = models.CharField(max_length=13,null=False)
    
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
    productName = models.CharField(max_length=100,null=False)
    amount = models.PositiveIntegerField(null=False)
    saleDate = models.DateTimeField(auto_now_add=True)
    subtotal = models.PositiveIntegerField(null=False)
    iva = models.PositiveBigIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)