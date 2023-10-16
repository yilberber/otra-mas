import pandas as pd 
import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import html
from PIL import Image 

niveles_construccion = (
    "Hasta 3 niveles",
    "Entre 4 y 10 niveles",
    "Entre 11 y 20 niveles",
    "Mayor de 20 niveles")

cargas_máximas=(
    "Menores de 800 kN",
    "Entre 801 y 4000 kN",
    "Entre 4001 y 8000 kN",
    "Mayores de 8000 kN"
)

categoría_construcción=(
    "Baja",
    "Media",
    "Alta",
    "Especial"
)
clasificación_categorias = pd.DataFrame ({
    "Niveles": niveles_construccion,
    "Cargas máximas": cargas_máximas,
    "Categoría": categoría_construcción
})



