import geojson

# List of allowed names
allowed_names = [
    "SA-2", "SA-6", "SA-3", "S300P", "SA-5", "Hawk", "Patriot", "HQ-2", "HQ-7", 
    "HQ-12", "S-300PMU", "S-300PMU-1", "S-300PMU-2", "HQ-6D", "HQ-9", "SA-15", 
    "Chu-SAM", "S-300PT", "S-300PS", "S-300PM", "S-400", "S-300V"
]

def filter_geojson(input_file, output_file):
    # Load the input GeoJSON file
    with open(input_file, 'r') as f:
        data = geojson.load(f)

    # Filter the features based on the allowed names
    filtered_features = [
        feature for feature in data['features']
        if feature['properties'].get('name') in allowed_names
    ]

    # Create a new GeoJSON object with the filtered features
    filtered_geojson = geojson.FeatureCollection(filtered_features)

    # Write the filtered GeoJSON to a new file
    with open(output_file, 'w') as f:
        geojson.dump(filtered_geojson, f)

    print(f"Filtered GeoJSON saved to {output_file}")

# Example usage:
input_geojson_file = 'data.geojson'
output_geojson_file = 'filtered_output.geojson'
filter_geojson(input_geojson_file, output_geojson_file)
