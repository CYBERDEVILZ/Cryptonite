import pandas as pd
import plotly.graph_objects as go
import plotly.express as ex
import retrieveinfo
df = pd.DataFrame({
                    "Latitude": [],
                    "Longitude": [],
                    "Place": []
                })

lat = retrieveinfo.location()[0]
long = retrieveinfo.location()[1]
place = retrieveinfo.location()[2]

df["Latitude"] = lat
df["Longitude"] = long
df["Place"] = place

mapbox_access_token = open(".map_token").read()

fig = go.Figure(go.Scattermapbox(
        lat=df["Latitude"],
        lon=df["Longitude"],
        mode='markers',
        hoverlabel=go.scattermapbox.Hoverlabel(
            bgcolor='#451a8a',
            bordercolor='white'
        ),
        marker=go.scattermapbox.Marker(
            size=14,
            color='#00ffdd'
        ),
        hovertext=df["Place"],
    ))

fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=float(lat[0]),
            lon=float(long[0])
        ),
        style="dark",
        pitch=40,
        zoom=3
    )
)

fig.show()