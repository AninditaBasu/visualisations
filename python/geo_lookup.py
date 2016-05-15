# libraries used: csv, geopy

# takes a CSV file with place names and returns another
# CSV file called "place_coords.csv" in the same directory
# as this script. The new file has the place names as well as
# the laltitude and longitude values

# read the data from file and write to a list

import csv

place_file = raw_input("Enter the name of the CSV file: ")
place_row = raw_input("Enter the column number that contains the places to look up: ")
place_row_header = raw_input("Enter the column heading of the column that contains the places to look up: ")

place_row = int(place_row)
coord_points = []

with open(place_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        coord_points.append(row)
#
# get the coordinates of the places
#
from geopy.geocoders import Nominatim
geolocator = Nominatim()
#
# iterate over the list but skip the first row (header row)
# and generate a new list with place coordinates
#
coord_points_list = []
templist = []
for item in coord_points:
    if item[place_row-1] != place_row_header:
        try:
            location = geolocator.geocode(item[place_row-1])
            lat = location.latitude
            lng = location.longitude
            print item[place_row-1], str(lat), str(lng)
        except:
            lat = ""
            lng = ""
        templist.append(item[place_row-1])
        templist.append(lat)
        templist.append(lng)
        coord_points_list.append(templist)
        templist = []

#
# write data to a file
#
with open("place_coord.csv", "wb") as f:
    writer = csv.writer(f, delimiter=',')
    for item in coord_points_list:
        writer.writerow(item)

