# ! import library
# ? Is it important to import this library
# ToDo: Have to add multiple makers

import folium
import pandas as pd
from folium.plugins import MarkerCluster

#load Data
data = pd.read_csv("us.txt")
lat = data['LAT']
lon = data["LON"]
elevation = data['ELEV']

#function to change color
def color_change(elevation):
    if elevation < 1000:
        return('green')
    elif (1000 <= elevation < 3000):
        return('orange')
    else:
        return('red')

# Create Base Map

map = folium.Map(location=[37.296933,-121.9574983], zoom_start=5, tiles="CartoDB dark_matter")

#Marker Cluster 
marker_cluster= MarkerCluster().add_to(map)  

# ? Multi markers handelling 
for lat,lon,elevation in zip(lat,lon,elevation):
    folium.CircleMarker(location=[lat,lon],radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color= 'grey', fill_opacity=0.9).add_to(marker_cluster)

# ? Save the map
map.save("map1.html")



