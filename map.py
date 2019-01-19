# import folium

# map = folium.Map(location=[28.5799217,77.0546595], zoom_start=8)

# map.save("map1.html")


import folium

#Create base map
map = folium.Map(location=[28.5799217,77.0546595], zoom_start = 8, tiles="Mapbox bright")

folium.Marker(location=[28.5799217,77.0546595],popup="Punjab National National Bank", icon=folium.Icon(color='gray')).add_to(map)

#Save the map
map.save("map1.html")