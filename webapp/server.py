from flask import Flask
from dash import Dash
import dash_bootstrap_components as dbc

server = Flask(__name__)
server.config["TEMPLATES_AUTO_RELOAD"] = True
app = Dash(
    __name__,
    # assets_external_path='/assets',
    external_stylesheets=[dbc.themes.SLATE],
    server=server,
    suppress_callback_exceptions=True,
    title='Dashboard de Sensores'
)