import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import geopandas as gpd
from dash import Dash, html,dcc, callback, Input, Output
from PIL import Image 

izquierdo = dbc.Container(
    [
        html.H1('NUEVO SONDEO', style={'color':'#241E7D'}),
        html.Hr(),
        html.Div([
        ]),

        html.Div([
                html.H2('CATEGORIA DEL PROYECTO', style={'color':'#241E7D'}),
                html.H5('Niveles de construcción ', style={'color':'#04163E'}),
                dcc.Dropdown(
                    id = 'firstdropdown',
                    options = [
                        {'label': 'Hasta 3 niveles', 'value': 'nv3'},
                        {'label': 'Entre 4 y 10 niveles', 'value': 'nv4'},
                        {'label': 'Entre 11 y 20 niveles', 'value': 'nv11'},
                        {'label': 'Mayor de 20 niveles', 'value': 'nv20'},
                    ],
                    value = 'nv3'
                ),
                
                html.H5('Cargas máximas de servicio en columnas', style={'color':'#04163E'}),
                dcc.Dropdown(
                    id = 'seconddropdown',
                    options = [
                        {'label': 'Menores de 800 kN', 'value': 'M800'},
                        {'label': 'Entre 801 y 4000 kN', 'value': 'M801'},
                        {'label': 'Entre 4001 y 8000 kN', 'value': 'M4001'},
                        {'label': 'Mayores de 8000 kN', 'value': 'M8000'},
                    ],
                    value = 'M800'

                ), 
        html.Label(id='salidaPisos'),
            ]
        ),
        
    ],


    style={'background-color':'#E3E1FF'},

)

