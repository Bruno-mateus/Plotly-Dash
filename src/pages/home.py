import pandas as pd
from dash import dcc, html
from components.mapPlot import mapPlot

# Dados de teste
data = {
    'Estado': ['SP', 'PR', 'RJ'],
    'Reclamacoes': [120, 80, 150],
    'Estado_Nome': ['São Paulo', 'Paraná', 'Rio de Janeiro']
}

data2 = {
    'Estado': ['SP', 'PR', 'RJ'],
    'Reclamacoes': [180, 60, 166],
    'Estado_Nome': ['São Paulo', 'Paraná', 'Rio de Janeiro']
}

df = pd.DataFrame(data)
 
def home():
    return html.Div([
        html.H1(dcc.Link('Page 2',href='/page2')),
        dcc.Graph(figure=mapPlot(df)),
        dcc.Graph(figure=mapPlot(data2))
        
    ])
