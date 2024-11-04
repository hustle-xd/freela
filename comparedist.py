from geopy.distance import geodesic
import csv

last={}

# Define the reference location (latitude, longitude)



  # Example: Los Angeles, CA
def comparedistance(reference_location):
    rangeid = []

# Define a list of other locations with their latitude and longitude
    with open(r"C:\Users\pande\OneDrive\Desktop\bot\bot\plugins\database\profile.csv", "r") as f:
        read = csv.DictReader(f)
        try:
            for i in read:

            
            
                print(i)
                a = i['id']


                lat=i['Latitude']
                long=i['Longitude']
                last[a]=[float(lat), float(long)]
        except:
            pass

    # Define the distance threshold in miles
    distance_threshold = 100

    # Function to check if a location is within the distance threshold
    def is_within_range(ref_loc, loc, threshold):
        distance = geodesic(ref_loc, loc).miles
        return distance < threshold

    # Find and print locations within the specified range
    print(f"Locations within {distance_threshold} miles of {reference_location}:")
    for i, j in last.items():
        if is_within_range(reference_location, j, distance_threshold):
            # print(f"- {}: {i} ({geodesic(reference_location, loc).miles:.2f} miles away)")
            rangeid.append(int(i))
    return rangeid


