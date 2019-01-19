# ! import library
# ? Is it important to import this library
# ToDo: Have to add multiple makers

import folium


# Create Base Map

map = folium.Map(location=[37.296933,-121.9574983], zoom_start=8, tiles="Mapbox bright")

# ? Multi markers handelling 
for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color="green")).add_to(map)

# ? Save the map
map.save("map1.html")


