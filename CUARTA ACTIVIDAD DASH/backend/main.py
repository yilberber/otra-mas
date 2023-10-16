import dash 
from dash import html,dcc
import dash_bootstrap_components as dbc

#importamos el backend
from backend.calculosondeos import clasificación_categorias

layout= clasificación_categorias

