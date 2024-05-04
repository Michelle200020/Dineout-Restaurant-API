from import_export import resources 
from .models import Restaurant
class RestaurantResource(resources.ModelResource):
     class Meta:
         model = Restaurant
         import_id_fields = ('id', 'restaurant_id')

        