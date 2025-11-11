import pandas as pd
import folium
from folium.plugins import MarkerCluster
import matplotlib.colors as mcolors


data = pd.read_csv("crop_data_india_300.csv")

if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
    import random
    data['Latitude'] = data['City'].apply(lambda x: random.uniform(8.0, 37.0))
    data['Longitude'] = data['City'].apply(lambda x: random.uniform(68.0, 97.0))

m = folium.Map(location=[22.5, 78.9], zoom_start=5, tiles="OpenStreetMap")


marker_cluster = MarkerCluster().add_to(m)

colors = list(mcolors.TABLEAU_COLORS.values())
unique_crops = data['Crop'].unique()
color_map = {crop: colors[i % len(colors)] for i, crop in enumerate(unique_crops)}

for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=6,
        color=color_map[row['Crop']],
        fill=True,
        fill_color=color_map[row['Crop']],
        popup=folium.Popup(
            f"<b>State:</b> {row['State']}<br>"
            f"<b>City:</b> {row['City']}<br>"
            f"<b>Crop:</b> {row['Crop']}<br>"
            f"<b>Rainfall:</b> {row['rainfall']} mm<br>"
            f"<b>Temperature:</b> {row['temperature']} °C",
            max_width=250
        )
    ).add_to(marker_cluster)

legend_html = """
<div 
style="position: fixed; bottom: 50px; left: 50px; width: 200px; 
background-color: white; border:2px solid grey; z-index:9999; font-size:14px;">
&nbsp;
<b>Crop Legend</b>
<br>
{}
</div>
""".format("<br>".join([f"&nbsp;<i style='color:{color_map[crop]};'>●</i> {crop}" 
                        for crop in unique_crops]))
m.get_root().html.add_child(folium.Element(legend_html))

# Save map
m.save("crop_distribution_map.html")
print("Map saved successfully as 'crop_distribution_map.html'")
