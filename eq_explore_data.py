from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('python_work/downloadingData/eq_data/eq_data_1_day_all.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(f"{mags[:3]} mags")
print(f"{lons[:3]} lons")
print(f"{lats[:3]} lats")

# Create a more readable version of the data file.
path = Path('python_work/downloadingData/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)