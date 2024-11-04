from geopy.geocoders import Nominatim

# Create a geolocator object
geolocator = Nominatim(user_agent="tryingit (for my program)")

# Function to get latitude and longitude
def get_lat_lon(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return [location.latitude, location.longitude]
        else:
            return None
    except Exception as e:
        print(e)





