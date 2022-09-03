import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])

def colourmaker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000 :
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6)

fgv = folium.FeatureGroup(name = "Volcanoes")

for i,j,k in zip(lat,lon,el):
    fgv.add_child(folium.CircleMarker(location=(i,j), radius=6, popup=str(k) + "m", fill_color=colourmaker(k),color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name= "Population")

fgp.add_child(folium.GeoJson(data = open("115 world.json",'r',encoding='utf-8-sig').read() ,style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000< x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
