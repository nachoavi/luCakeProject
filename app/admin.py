from django.contrib import admin
from .models import ClientContacts,ProductsInventory,Sales,CategoryProduct

# Register your models here.
admin.site.register(ClientContacts)
admin.site.register(ProductsInventory)
admin.site.register(Sales)
admin.site.register(CategoryProduct)