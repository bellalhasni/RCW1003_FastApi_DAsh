import dash
from dash import html, dcc
import requests

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

EXTERNAL_API_URL = "http://127.0.0.1:8000/info"

def get_external_info():
    try :
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e :
        return{
            "date":"N/A",
            "time":"N/A",
            "weather":{
                "city":"N/A",
                "temperature":"N/A",
                "description":"N/A"
            }
            
        }
    
info = get_external_info()
print("info",info)
weather = info.get("weather", {})

app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/'),
        "|",
        html.A('Logout', href='/logout'),
    ], style={'marginTop': 25}),
    
    html.H2("Bar Graph"),
    dcc.Graph(
        id="exmpl-1",
        figure={
            "data": [
                {"x": [2, 5, 7], "y": [8, 3, 9], "type": "bar", "name": "exmp1"},
                {"x": [5, 3, 8], "y": [6, 2, 5], "type": "bar", "name": "exmp2"}
            ]
        }
    ),
    
    
    html.H2("Line Graph"),
    dcc.Graph(
        id="exmpl-2",
        figure={
            "data": [
                {"x": [8,10,14], "y": [13,8,1], "type": "line", "name": "exmp3"},
                {"x": [4,20,19], "y": [16,7,2], "type": "line", "name": "exmp4"}
            ]
        }
    ),
    
    
    html.H2("Scatter Graph"),
    dcc.Graph(
        id="exmpl-3",
        figure={
            "data": [
                {"x": [8,10,14,7], "y": [13,8,1,3], "type": "scatter","mode":"markers", "name": "exmp5"},
                {"x": [4,20,19], "y": [16,7,2], "type": "scatter","mode":"markers", "name": "exmp6"}
            ]
        }
    ),
    
    html.H2("Pie Chart"),
    dcc.Graph(
        id="exmpl-4",
        figure={
            "data": [
                {"labels": ["A","B","C","D"], "values": [13,8,1,3], "type": "pie","name": "exmp7"} 
            ]
        }
    ),
    html.H2("Info Temperature"),
    html.Div(className="info-box", children=[
        html.H2(f"Aujourd'hui est {info.get('date')} et il est {info.get('time')}"),
        html.P(f"city : {weather.get('city')}"),
        html.P(f"température : {weather.get('temperature')}"),
        html.P(f"description : {weather.get('description')}")
    ])
    
    
])


server = app.server
