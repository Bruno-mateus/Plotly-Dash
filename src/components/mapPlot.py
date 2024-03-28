import pandas as pd
import plotly.express as px
import json
from urllib.request import urlopen






def mapPlot(df):
    state_id_map = {}

    with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
        Brazil = json.load(response) 
        Brazil



    for feature in Brazil ['features']:
        feature['id'] = feature['properties']['name']
        state_id_map[feature['properties']['sigla']] = feature['id']


    fig = px.choropleth(
    df, #soybean database
    locations = 'Estado_Nome', 
    geojson = Brazil, #shape information
    color = "Reclamacoes", 
    hover_name = 'Estado', 
    hover_data =['Reclamacoes'],
    title = "Reclamacoes", 
    #animation_frame = 'ano' 
    
    )
    fig.update_geos(fitbounds = "locations")
    return fig