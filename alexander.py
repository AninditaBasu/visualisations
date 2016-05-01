# libraries used: csv, geopy, ...

# read the data from file and write to a list
import csv
routepoints = []
with open('./data/alexander.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        routepoints.append(row)
#
# data is a list of dates and places
# get the coordinates of the places
#
from geopy.geocoders import Nominatim
geolocator = Nominatim()
#
# iterate over the list but skip the first row (header row)
# and generate a new list with place coordinates
#
routecoords = []
templist = []
for item in routepoints:
    if item[1]!="Place":
        try:
            location = geolocator.geocode(item[1])
            lat = location.latitude
            long = location.longitude
        except:
            lat = ""
            long = ""
        templist.append(item[0])
        templist.append(item[1])
        templist.append(lat)
        templist.append(long)
        routecoords.append(templist)
        templist = []
print routecoords

#
# to write back to a csv file, a heading row is needed
header = []
header.append("Date")
header.append("Place")
header.append("Latitude")
header.append("Longitude")
routecoords.insert(0, header)

with open("./data/alexander_coord.csv", "wb") as f:
    writer = csv.writer(f, delimiter=',')
    for item in routecoords:
        writer.writerow(item)

# find the min and max latitude and longitude, to define a map area
