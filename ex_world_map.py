from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('python_work/downloadingData/eq_data/world_fires_data_Global_24h.csv')
lines = path.read_text().splitlines()

# Examine all world fires data in the dataset.
reader = csv.reader(lines)
header_row = next(reader)

# Extract data
lats, lons, brights = [], [], []
for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        continue
    else:
        lats.append(lat)    
        lons.append(lon)
        brights.append(bright)

title = 'Active Fire Data'

fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title, 
        color=brights,
        color_continuous_scale='aggrnyl',
        labels={'color':'magnitude'},
        projection='natural earth',
        )

fig.show()