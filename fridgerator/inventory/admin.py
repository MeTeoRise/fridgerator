from django.contrib import admin
from .models import Item, ShoppingList, Alert, Maintenance, Setting

admin.site.register(Item)
admin.site.register(ShoppingList)
admin.site.register(Alert)
admin.site.register(Maintenance)
admin.site.register(Setting)
