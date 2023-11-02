from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('users/',views.usersTable,name='usersTable'),
    path('users/create',views.createUser,name='createUser'),
    path('users/update/<int:id>',views.updateUser,name='updateUser'),
    path('users/delete/<int:id>',views.deleteUser,name='deleteUser'),
    path('products/',views.productsTable,name='productsTable'),
    path('products/create',views.createProducts,name='createProducts'),
    path('products/delete/<int:id>',views.deleteProducts,name='deleteProducts'),
    path('products/update/<int:id>',views.updateProduct,name='updateProducts'),
    path('sales/',views.salesTable,name='salesTable'),
    path('sell/',views.sell,name='sell'),
    path('clientContacts/',views.clientContacts,name='clientContacts'),
    path('clientContacts/create/',views.createClientContacts,name='createClientContacts'),
    path('clientContacts/update/<int:id>',views.updateClientContacts,name='updateClientContacts'),
    path('clientContacts/delete/<int:id>',views.deleteClientContacts,name='deleteClientContacts'),
    path('recipes/',views.recipes,name='recipes'),
    path('recipesForm/',views.recipesForm,name='recipesForm'),
    path('suppliers/',views.suppliersTable,name="suppliersTable"),
    path('suppliers/create/',views.createSuppliers,name="createSuppliers"),
    path('suppliers/update/<int:id>',views.updateSuppliers,name='updateSuppliers'),
    path('suppliers/delete/<int:id>',views.deleteSuppliers,name='deleteSuppliers'),
    
]