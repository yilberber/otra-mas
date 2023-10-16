import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#importamos el frontend
from frontend.main import layout
from backend.calculosondeos import*
import math
import pandas as pd
from PIL import Image 
from dash import html
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
                
app.layout = layout

@app.callback(
    Output('salidaPisos','children'),
    Input('firstdropdown','value'),
    Input('seconddropdown','value'),
)

def numeroPisos(firstdropdown, seconddropdown):
    if  firstdropdown == 'nv3':
        if seconddropdown == 'M800':
            categoria = 'categoria baja'
            numerosondeos = 'mínimo 3'
            profundidadmin = '6 metros'

        elif seconddropdown == 'M801':
            categoria = 'categoria media'
            numerosondeos = 'mínimo 4'
            profundidadmin = '15 metros'
        elif seconddropdown == 'M4001':
            categoria = 'categoria alta'
            numerosondeos = 'mínimo 4'
            profundidadmin = '25 metros'
        elif seconddropdown == 'M8000':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'

    elif firstdropdown == 'nv4':
        if seconddropdown == 'M800':
            categoria = 'categoria media'
            numerosondeos = 'mínimo 4'
            profundidadmin = '15 metros'

        elif seconddropdown == 'M801':
            categoria = 'categoria media'
            numerosondeos = 'mínimo 4'
            profundidadmin = '15 metros'
        elif seconddropdown == 'M4001':
            categoria = 'categoria alta'
            numerosondeos = 'mínimo 4'
            profundidadmin = '25 metros'
        elif seconddropdown == 'M8000':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'

    elif firstdropdown == 'nv11':
        if seconddropdown == 'M800':
            categoria = 'categoria alta'
            numerosondeos = 'mínimo 4'
            profundidadmin = '25 metros'

        elif seconddropdown == 'M801':
            categoria = 'categoria alta'
            numerosondeos = 'mínimo 4'
            profundidadmin = '25 metros'
        elif seconddropdown == 'M4001':
            categoria = 'categoria alta'
            numerosondeos = 'mínimo 4'
            profundidadmin = '25 metros'
        elif seconddropdown == 'M8000':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'

    elif firstdropdown == 'nv20':
        if seconddropdown == 'M800':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'

        elif seconddropdown == 'M801':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'
        elif seconddropdown == 'M4001':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'
        elif seconddropdown == 'M8000':
            categoria = 'categoria especial'
            numerosondeos = 'mínimo 5'
            profundidadmin = '30 metros'
    else: 
        mensaje = 'Ingrese un dato valido'

    #resultado = [
        #'EDIFICIO: ' + str(categoria),
        #'NUMERO DE SONDEOS: ' + str(numerosondeos),
        #'PROFUNDIDAD MÍNIMA DE SONDEOS: ' + str(profundidadmin)
    #]

    # Convertir el resultado en una lista como código Python
    # resultado_codigo = '[' + ', '.join([f"'{item}'" for item in resultado]) + ']'
    
    return dbc.Container([
        html.Hr(),
        html.H2('La edificación es:',style={'color':'#001BBD'}),
        html.H4([categoria]),
        html.H2('Cantidad de sondeos a realizar:',style={'color':'#001BBD'}),
        html.H4([numerosondeos]),
        html.H2('La profundidad mínima de sondeos es de:',style={'color':'#001BBD'}),
        html.H4([profundidadmin]),
        ])

    # Ejemplo de uso:
firstdropdown = 'nv3'
seconddropdown = 'M800'

resultado_lista_codigo = numeroPisos(firstdropdown, seconddropdown)
print(resultado_lista_codigo)
    
    

niveles_construccion = (
    "Hasta 3 niveles",
    "Entre 4 y 10 niveles",
    "Entre 11 y 20 niveles",
    "Mayor de 20 niveles"
)

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

if __name__ == '__main__' :
    app.run_server(debug=True)
