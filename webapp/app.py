# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

THEME = 'bootstrap'
app = Dash(
    __name__,
    external_stylesheets=[
        getattr(dbc.themes, THEME.upper()),
        f'https://cdn.jsdelivr.net/gh/tcbegley/dash-bootstrap-css@main/dist/{THEME.lower()}/bootstrap.min.css'
    ],
    suppress_callback_exceptions=True
)

colors = {
    'background': '#ffffff',
    'text': '#7FDBFF'
}

str_datafolder = "kaggle-survey-2022"
str_datafile = "kaggle_survey_2022_responses.csv"
str_filepath = os.path.join(str_datafolder,str_datafile)
df_main = pd.read_csv(str_filepath, skiprows=[1]) # ignore first row which is question statement
df_questions = pd.read_csv(str_filepath, nrows=1) # question statements

Q3_counts = df_main.Q3.value_counts()

Q3_counts = pd.DataFrame({"Gender":Q3_counts.keys(),
                          "Count":Q3_counts.values})


fig = px.bar(Q3_counts, x="Gender", y="Count", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='2022 Kaggle Machine Learning & Data Science Survey',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='The most comprehensive dataset available on the state of ML and data science.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)