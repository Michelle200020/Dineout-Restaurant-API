from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantData(APIView):
    def get(self, request ,name):
        try:
            restaurant = Restaurant.objects.get( name=name)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({"message": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)





# import pandas as pd
# from .models import Restaurant  # Import your Django model




# def save_restaurants_from_excel(file_path):
#     # Read the CSV file into a DataFrame
#     df = pd.read_excel(file_path)

#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         # Create a new Restaurant object and populate its fields from the DataFrame row
#         restaurant = Restaurant(
#             restaurant_id=row['restaurant_id'],
#             name=row['name'],
#             cuisines=row['cuisines'],
#             price=row['price'],
#             location=row['location'],
#             open_from=row['open_from'],
#             open_till=row['open_till'],
#             offer=row['offer'],
#             offer_type=row['offer_type'],
#             restaurant_type=row['restaurant_type'],
#             features=row['features'],
#             rating=row['rating'],
#             votes=row['votes'],
#             reviews=row['reviews'],
#             outlet_count=row['outlet_count']
#         )
#         # Save the Restaurant object to the database
#         restaurant.save()

# # Call the function and provide the path to your CSV file


# def index(request):
#     save_restaurants_from_excel(r"C:\Users\miche\OneDrive\Desktop\Christ_University-Bsc_Data_Science\Semester 4\Full Stack Development\Final_Dineout_Restaurant.xlsx")
#     return {}