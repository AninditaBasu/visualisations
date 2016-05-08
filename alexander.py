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
            lng = location.longitude
        except:
            lat = ""
            lng = ""
        templist.append(item[0])
        templist.append(item[1])
        templist.append(lat)
        templist.append(lng)
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


# this plot works for the time being
#
# to be improved. pull data from csv
#
#%matplotlib inline
#
#coords = [(40.82,22.38),(32.32,44,25),(38.79,22.54),(42.71,24.91),(40.2,26.4),(38.29,28.02),(37.02,27.25),(36.15,29.59),(33.27,35.2),(29.2,25.51),(29.93,52.89),(34.79,48.51),(31.62,65.73),(39.62,66.97),(32.48,72.9),(30.19,71.46),(39.45,46.44)]
#places = ('Pella','Babylon','Thermopylae','Botev','Dardanelles','Sardis','Halicarnassus','Lycia','Tyre','Siwa','Persepolis','Hamadan','Kandahar','Samarkand','Bhera','Multan','Susa')
#
#import matplotlib.pyplot as plt
#
#x = []; y=[]
#for point in coords:
#   y.append(point[0])
#   x.append(point[1])
#
#plt.suptitle("Alexander's route", fontsize=16)
#plt.xlabel('latitude', fontsize=12)
#plt.ylabel('longitude', fontsize=12)
#plt.scatter(x,y)
#for i, txt in enumerate(places):
#    plt.annotate(txt, (x[i],y[i]))
#plt.show()
#
