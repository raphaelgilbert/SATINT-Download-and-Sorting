import json

dict = { "type": "FeatureCollection", "features": [{"geometry": [42.000000, 0.000000]}, {"Name": "Sa2"}]
        
        }

ListofCOOR = [[42.0, 0.0], [40.0, 0.0]]
ListofNAME = ["SA2", "SA3"]

Jsonfinal = []
for i in range(len(ListofCOOR)) : 
    Jsonfinal.append({"Name" : ListofNAME[i], "coordinates": ListofCOOR[i]})

print(Jsonfinal)

print(json.dumps(Jsonfinal, indent=4))

