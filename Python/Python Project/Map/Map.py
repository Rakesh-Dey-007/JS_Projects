import folium
import pandas as pd

try:
    # Attempt to read the Excel file
    data = pd.read_excel("IIT Ranking.xlsx")

    # Extract data from the dataframe
    iit_ranking = list(data["IIT Ranking"])
    Collage_name = list(data["IIT Collage"])
    Nirf_score = list(data["NIRF Score"])
    lat = list(data["Latitude"])
    lon = list(data["Longitude"])
    Img = list(data["Image"])

    fg = folium.FeatureGroup("map")
    
    try:
        # Attempt to read the GeoJSON file
        fg.add_child(folium.GeoJson(data=(open("india_states.json", "r", encoding="utf-8-sig").read())))
    except FileNotFoundError:
        print("Error: The 'india_states.json' file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the GeoJSON file: {e}")

    # Add markers to the map
    for rank, name, score, lati, longi, ima in zip(iit_ranking, Collage_name, Nirf_score, lat, lon, Img):
        fg.add_child(folium.Marker(
            location=[lati, longi],
            popup=(
                f"<b>Collage Name : </b>{name}<br>"
                f"<b>Rank among IIT in India : </b>{rank}<br>"
                f"<b>NIRF Score : </b>{score}<br>"
                f'<img src="{ima}" height="142" width="290">'
            ),
            icon=folium.Icon(color="red")
        ))

    # Create the map and add the feature group
    map = folium.Map(location=[20.0000, 75.0000], zoom_start=4)
    map.add_child(fg)

    # Save the map to an HTML file
    map.save("Map.html")
    print("Map created successfully!")

except FileNotFoundError:
    print("Error: The 'IIT Ranking.xlsx' file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
