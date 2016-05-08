#
# To convert the tab-delimited text file to CSV
# Data was downloaded from National Geophysical Data Center
# https://www.ngdc.noaa.gov/hazard/earthqk.shtml
# in tab-delimited format and converted to CSV first by
# using the following code, commented out.
# comment out code begin===
#
#import csv
#txt_file = r"./data/signif.txt"
#csv_file = r"./data/earthquakes.csv"
#in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
#out_csv = csv.writer(open(csv_file, 'wb'))
#out_csv.writerows(in_txt)
#
# comment out code end===

# read the data from file and write to a list of tuples
import csv
from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

earthquakes = []
entry = ()
quake_year = ()
quake_country = ()
quake_place = ()
quake_lat = ()
quake_long = ()
deaths = []
with open('./data/earthquakes.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[2] == "YEAR":
            qyr = (row[2]).strip()
            qyr = int(qyr)
            quake_year += (qyr,)
            qcountry = (row[17]).strip()
            quake_country += (qcountry,)
            qplace = (row[19]).strip()
            quake_place += (qplace,)
            y = (row[20]).strip()
            x = (row[21]).strip()
            if not y == "":
                y = float(y)
                quake_lat += (y,)
            if not x == "":
                x = float(x)
                quake_long += (x,)
            d = (row[23]).strip()
            if not d == "":
                d = int(d)
                deaths.append(d)
            entry = (qyr, qcountry, qplace, y, x, d)
            earthquakes.append(entry)
#
# if writing back to a CSV file, a header is needed
#header = []
#header.append("Year")
#header.append("Country")
#header.append("Location")
#header.append("Latitude")
#header.append("Longitude")
#earthquakes.insert(0, header)
#
print earthquakes
earthquake_count = len(earthquakes)
country_count = len(Counter(quake_country))

s = str(quake_year[0])
s = s[1:]+" BC"

print "------------------------------------"
print earthquake_count, "earthquakes between", s, "and", quake_year[earthquake_count -1], "AD in", country_count, "countries"
print "------------------------------------"

max_lat = max(quake_lat)
min_lat = min(quake_lat)
max_lng = max(quake_long)
min_lng = min(quake_long)

for entry in earthquakes:
    if entry[3]==max_lat:
        print "Farthest north: In",entry[0],"at",entry[2].title(),entry[1].title(),"(location coordinates:",entry[3],"lat,",entry[4],"long)"
    elif entry[3]==min_lat:
        print "Farthest south: In",entry[0],"at",entry[2].title(),entry[1].title(),"(location coordinates:",entry[3],"lat,",entry[4],"long)"
    if entry[4]==max_lng:
        print "Farthest east: In",entry[0],"at",entry[2].title(),entry[1].title(),"(location coordinates:",entry[3],"lat,",entry[4],"long)"
    elif entry[4]==min_lng:
        print "Farthest west: In",entry[0],"at",entry[2].title(),entry[1].title(),"(location coordinates:",entry[3],"lat,",entry[4],"long)"
print "------------------------------------"

deaths.sort(reverse=True)
deaths_heavy = []
i = 0
for item in deaths:
    if item>=100000:
        deaths_heavy.append(deaths[i])
    i += 1
print "High death toll (more than 100,000 dead):"
deaths_heavy_hbar_xaxis = ()
deaths_heavy_hbar_yaxis = ()
deaths_heavy_hbar_annotation = ()

for item in deaths_heavy:
    for entry in earthquakes:
        if item == entry[5]:
            print entry[0], entry [1], entry[5]
            deaths_heavy_hbar_xaxis += (entry[5],)
            deaths_heavy_hbar_yaxis += (entry[1],)
            deaths_heavy_hbar_annotation += (entry[0],)
print "------------------------------------"

# to plot number of quakes by country, highest
country_name = ()
country_count = ()
country_aggregates = Counter(quake_country).most_common()
for item in country_aggregates:
    if item[1]>=200:
        country_name += (item[0].title(),)
        country_count += (item[1],)
#
n_groups = len(country_name)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.75
bars = plt.bar(index, country_count, bar_width, alpha=opacity, color='r')
#plt.xlabel('Country')
#plt.ylabel('Number of earthquakes (2150 BC to 2016 AD)')
plt.title('Countries with most earthquakes (2150 BC to 2016 AD)')
plt.xticks(index + bar_width, country_name)
plt.tight_layout()
plt.show()
plt.savefig('./data/earthquakes1')
plt.clf()

# to plot casualties by country, highest
y_pos = np.arange(len(deaths_heavy_hbar_annotation))
deaths = deaths_heavy_hbar_xaxis
error = np.random.rand(len(deaths_heavy_hbar_annotation))
bar_width = 0.25
opacity = 0.35
plt.barh(y_pos, deaths, xerr=error, align='center', alpha=opacity, color='r')
plt.yticks(y_pos, deaths_heavy_hbar_annotation)
#plt.xlabel('Deaths')
#plt.ylabel('Year')
#plt.title('More than 100,000 dead')
plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
plt.show()
plt.savefig('./data/earthquakes2')
plt.clf()