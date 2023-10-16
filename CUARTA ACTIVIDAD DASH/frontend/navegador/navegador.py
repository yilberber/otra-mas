import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container([
    html.H1('SONDEO CIVIL PRO', style={'color':'white'}),
    html.Hr(),
    html.H2('¿Quienes Somos?', style={'color':'lightgrey'}),
    html.Hr(),
    html.H5('La mejor app diseñada para simplificar y optimizar el proceso de determinar la cantidad de sondeos necesarios en proyectos de obras civiles', style={'color':'lightgrey'}),
    
    html.Hr()
    

])