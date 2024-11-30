import geojson
import pprint as pp


with open('data.geojson', 'r') as file:
    datageo = geojson.load(file)
a = 0
for i in datageo['feature'] : 
    if i['properties']['name'] == 'Empty SA-2 site' or i['properties']['name'] == 'Empty HAWK site' or i['properties']['name'] == 'Empty SA-3 site' or i['properties']['name'] == 'Empty SA-4 site' or i['properties']['name'] == 'Empty SA-5 site' or i['properties']['name'] == 'Empty SA-6 site' or i['properties']['name'] == 'Empty S-300P site' :
            geojson


dataclean['features'] = [feature in datageo['features'] if not datageo['features']['properties']['name'] == 'Empty SA-2 site' or i['properties']['name'] == 'Empty HAWK site' or i['properties']['name'] == 'Empty SA-3 site' or i['properties']['name'] == 'Empty SA-4 site' or i['properties']['name'] == 'Empty SA-5 site' or datageo['features']['properties']['name'] == 'Empty SA-6 site' or datageo['features']['properties']['name'] == 'Empty S-300P site'





for feature in datageo['features'] :
    a += 1

print(a)