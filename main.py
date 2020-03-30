#Running the file
#go to the directory where this Folder is
#Now >> export FLASK_DEBUG=1
# >> flask run
# Copy link of local host

import json
import math as Math

filename = "VacantLand_Dallas"  # File for Property for Sale Coordinates
filename2 = "DallasHospitals"  # File for Hospital Coordinates

with open(filename + '.json', 'r') as file:  # Loading json data of Property for Sale
    properties_json = json.load(file)
with open(filename2 + '.json', 'r') as file2:  # Loading json data of Hospital
    properties_json2 = json.load(file2)

lat1 = list()
lon1 = list()
lat2 = list()
lon2 = list()
add = list()

# Assigning variables, the keys for latitude and longitude in json file
lat = 'latitude'
lon = 'longitude'
prop_address = 'address'
title = 'title'
i = 0

# Storing json data of Lat and Long. of each file in a separate list respectively

for properties in properties_json:
    lat1.append(properties[lat])
    lon1.append(properties[lon])
    add.append(properties[prop_address][title])
    ##print(lat1[i] , lon1[i])
    i = i + 1
print("----------------------------------------------------------------------------------------------------------")
i = 0
for properties in properties_json2:
    lat2.append(properties[lat])
    lon2.append(properties[lon])
    i = i + 1


# Calculating distance between land on sale and nearby hospital using standard formulae based on Latitude and Longitude
def degreesToRadians(degrees):
    return degrees * Math.pi / 180;


def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2):
    earthRadiuskm = 6371;

    dLat = degreesToRadians(lat2 - lat1);
    dLon = degreesToRadians(lon2 - lon1);

    lat1 = degreesToRadians(lat1);
    lat2 = degreesToRadians(lat2);

    a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(
        lat2);
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return (earthRadiuskm * c)


## lat1 = int(input("Enter latitude1 :"))
## lon1 = int(input("Enter longitude1 :"))
## lat2 = int(input("Enter latitude2 :"))
## lon2 = int(input("Enter longitude2 :"))
distance = list()
latitude = list()
longitude = list()
num_Hosp = list()
address = list()

# lath = {}
# lonh = {}

# def in_range_check(latt, lont, lath, lonh, count, j):
#     #for j in range(0,len(lon1)):
#     dis = distanceInKmBetweenEarthCoordinates(latt, lont, lath, lonh) #
#     if(dis<=3 or j <= len(lath)-1):
#         count = count+1  #Counting number of such hospitals
#         in_range_check(latt, lont, lath, lonh, count, j+1)
#     else:
#         return count
# j=0
for i in range(0, len(lat1)):
    count = 0
    for j in range(len(lat2)):
        dis = distanceInKmBetweenEarthCoordinates(lat1[i], lon1[i], lat2[j], lon2[j])

        # Selecting the Property having a hospital in the range of 3Km
        if (dis <= 1):
            count = count + 1  # Counting number of such hospitals
    ##count = in_range_check(lat1[i], lon1[i], lat2, lon2, 0, 0)

    if count > 0:  # Check for whether the given property has at least one hospital in the given range
        latitude.append(lat1[i])
        longitude.append(lon1[i])
        address.append(add[i])
        num_Hosp.append(count)
    distance.clear()

#print("The best places for setting up Health Care Services are:")
#print("Address", "  ,", "Latitude", " ,", "Longitude", "  --> Number of nearby Hospitals")
center = list()
for i in range(len(address)):
    center.append({'address': address[i], 'lat': latitude[i], 'lng': longitude[i]})

# Checking for the property with minimum number of Hospitals or no Hospitals in the given range
# num = 0
# for i in range(0, len(num_Hosp)):
#     if num_Hosp[i] == min(num_Hosp):
#         print(address[i], ",", latitude[i], ",", longitude[i], " -->", num_Hosp[i])
#         num = num + 1
#print("Number of total Locations : ", num)
#print(center)
##print(max(distance))
## print("xxxxxxxxxxxxxxxxxxxxxxxx")
## # for d in distance:
## #     if(d<10):
## #         print(d)
## for l in length:
##     if(l>=0 and l<5):
##         print(l)
from flask import Flask, render_template
app = Flask(__name__)
        #{'lat' : '32.779167', 'lng' : '-96.808891'}]
@app.route("/")

def home():
    return render_template('index.html')

@app.route("/about")

def about():
    return render_template('about.html')

@app.route('/contact')

def contacts():
    return render_template('contact.html')

@app.route("/services")
#decorator, just a way to add functionality to ezisting function
def services():
    return render_template('services.html', coords = center)


if __name__ == "__main__":
    app.run(debug=True)


