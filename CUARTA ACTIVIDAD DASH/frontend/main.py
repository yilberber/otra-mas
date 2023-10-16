import dash 
from dash import html,dcc
import dash_bootstrap_components as dbc

#importamos el frontend
from frontend.navegador.navegador import navegador
from frontend.derecho.derecho import derecho
from frontend.izquierdo.izquierdo import izquierdo

layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador,md=12, style={'background-color':'#05165F'}),
        dbc.Col(izquierdo,md=8, style={'background-color':'#E3E1FF'}),
        dbc.Col(derecho,md=4, style={'background-color':'#7AA0F6'})
    ])

])