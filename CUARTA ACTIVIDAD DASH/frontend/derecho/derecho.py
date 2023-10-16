import dash
import dash_bootstrap_components as dbc
from dash import html

derecho = dbc.Container([
     
        html.H2('Niveles de construcción'),
        dbc.Row([
        dbc.Col(["Relacione la cantidad de niveles o plantas con la que contará su edificación. Para la definición del número de niveles se incluirán todos los pisos del proyecto, sótanos,terrazas y pisos técnicos."],md=12,style={'background-color':'#7AA0F6'}),
        html.H2('Cargas máximas de servicio en columnas'),
        dbc.Col(["Para las cargas máximas  de servicio se aplicará la combinación de carga muerta más la carga viva debida a la ocupación de la edificación. Esta información se obtiene de los diseños anteriormente planteados"],md=12,style={'background-color':'#7AA0F6'}),
        html.Hr(),

        html.H2('Datos del proyecto'),
        html.Hr(),
        html.Label('Nombre:'),
        dbc.Input(value="Nombre"),
        html.Label('Localización:'),
        dbc.Input(value="Localización"),
        html.Label('Fecha Inicio:'),
        dbc.Input(value="Fecha", type="date"),
        html.Label('Fecha Fin:'),
        dbc.Input(value="Fecha", type="date"),

    ])
    
])