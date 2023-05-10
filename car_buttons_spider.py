
# Library to Use Dash in Notebooks
from jupyter_dash import JupyterDash
# Dash HTML Components Library
from dash import html
# Dash Core Components Library
from dash import dcc
from dash import dash_table
from dash.dependencies import Input, Output
# Plotly Express Library for Graphics
import plotly.express as px

import dash_bootstrap_components as dbc

import serial     # library used to communicate with serial port
import re         # library used to extract data from string
import time       # library used to create periodic reading event
 

ser = serial.Serial()  # create a serial instance
ser.port = 'COM8'      # set the port number
ser.baudrate = 9600 
ser.open()

def car_control(ser, command):
    read_command = (command+'\n')
    ser.write(read_command.encode("utf-8"))
    #print(ser.readline())
       

app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Button("Forward", id ="Forward", color="primary", n_clicks=0, class_name="me-1"),     
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Button("Left",id="Left", color="succes", n_clicks=0, class_name="me-1"),
            dbc.Button("Stop",id="Stop", color="danger", n_clicks=0, class_name="me-1"),
            dbc.Button("Right",id="Right", color="warning", n_clicks=0, class_name="me-1"),
        ])   
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Button("Backward", id="Backward", color="info", n_clicks=0, class_name="me-1"),
        ])   
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Span(id="message"),
        ])
    ]),
    
])


forward_n_click=0
stop_n_click=0
backward_n_click=0
right_n_click=0
left_n_click=0

@app.callback(
    Output(component_id="message", component_property='children'),
    Input(component_id="Forward", component_property='n_clicks'),
    Input(component_id="Stop", component_property='n_clicks'),
    Input(component_id="Backward", component_property='n_clicks'),
    Input(component_id="Right", component_property='n_clicks'),
    Input(component_id="Left", component_property='n_clicks')
)
def button_click(forward, stop, backward, right, left ):
    message ='Waiting for a command'
    
    global forward_n_click
    global stop_n_click
    global backward_n_click
    global right_n_click
    global left_n_click
    
    if forward == forward_n_click:
        pass
    else:
        forward_n_click=forward
        car_control(ser, "Forward")
        print(forward)
        message='forward clicked'
      
    if backward!= backward_n_click:
        car_control(ser, "Backward")  
        message="backward clicked"
        print(backward)
        backward_n_click = backward
    else:
        pass
      
    if right!=right_n_click:
        car_control(ser, "Right")  
        message="right clicked"
        print(right)
        right_n_click=right
    else:
        pass
    
    if stop !=stop_n_click:
        car_control(ser, 'Stop') 
        message='Stop'
        print(stop)
        stop_n_click=stop
    else:
        pass
    
    if left !=left_n_click: 
        car_control(ser, 'Left') 
        message='left'
        print(left)
        left_n_click=left
    else:
        pass
      
    return message

#Execution
app.run_server(debug=True, mode='external', port=8055)
