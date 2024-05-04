from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [ 'restaurant_id', 'name', 'cuisines', 'price', 
    'location', 'open_from', 'open_till', 'offer', 'offer_type', 
    'restaurant_type', 'features', 'rating', 'votes', 'reviews', 
    'outlet_count'
]
