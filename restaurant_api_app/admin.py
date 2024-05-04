from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from .resource import RestaurantResource  
from .models import Restaurant
class RestaurantAdmin(ImportExportModelAdmin):
     resource_class = RestaurantResource      
admin.site.register(Restaurant, RestaurantAdmin)
