import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from apps import commonmodules,home,MonthlyData,navigation
import data_m_graphs as grp
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("GOPD TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("25,676", id="card-value",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)
card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("CWC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("2,507", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif", "color": "blue",}),
        ]
    )
)
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("ANC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("451", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif","color": "blue", }),
        ]
    )
)
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("PNC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("332", id="card-value", style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)
card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("FP TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("1105", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif" , "color": "blue", }),
        ]
    )
)
card5 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("TOTAL DELIVERIES SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("61", id="card-value", style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)

card6 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("NUMBER OF LIVES IMPROVED", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("0", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif","color": "blue", }),
        ]
    )
)


# Our dataframe
df = pd.read_csv('data/Tutini_Data.csv')
df1 = pd.read_csv('data/Tutini_Facility_Information_Data.csv')

fig = px.scatter(df, x='Year', y='GOPDClientsSeenPerMonth')
fig.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig.layout.plot_bgcolor = '#FFFFFF'
fig.layout.paper_bgcolor = '#fff'
fig.update_xaxes(showgrid=False)
fig.update_yaxes(range=(0,1000))

fig1 = px.scatter(df, x='Year', y='CWCClientsSeenPerMonth')
fig1.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig1.layout.plot_bgcolor = '#FFFFFF'
fig1.layout.paper_bgcolor = '#fff'
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(range=(0,300))

fig2 = px.scatter(df, x='Year', y='ANCClientsSeenPerMonth')
fig2.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig2.layout.plot_bgcolor = '#FFFFFF'
fig2.layout.paper_bgcolor = '#fff'
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(range=(0,50))

fig3 = px.scatter(df, x='Year', y='PNCClientsSeenPerMonth')
fig3.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig3.layout.plot_bgcolor = '#FFFFFF'
fig3.layout.paper_bgcolor = '#fff'
fig3.update_xaxes(showgrid=False)
fig3.update_yaxes(range=(0,30))

fig4 = px.scatter(df, x='Year', y='FPClientsSeenPerMonth')
fig4.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig4.layout.plot_bgcolor = '#FFFFFF'
fig4.layout.paper_bgcolor = '#fff'
fig4.update_xaxes(showgrid=False)
fig4.update_yaxes(range=(0,300))

fig5 = px.scatter(df, x='Year', y='DeliveriesCompletedPerMonth')
fig5.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig5.layout.plot_bgcolor = '#FFFFFF'
fig5.layout.paper_bgcolor = '#fff'
fig5.update_xaxes(showgrid=False)
fig5.update_yaxes(range=(0,10))


layout = html.Div([

    commonmodules.get_header(),
    commonmodules.get_tutini_menu(),
    html.H3('TUTINI MONTHLY DATA VISUALIZATION',
            style={"font-weight": "bold", "text-align": "center", "font-size": "18px",
                   'family': "Times New Roman,Times,serif", }),
    html.Div([dash_table.DataTable(

        id='Desc',
        columns=[{"Facility name": i, "id": i} for i in df1.columns],
        data=df1.to_dict('records'),
        style_table={'Height': 200, 'Width': 100, 'overflowX': 'auto'},
        style_header={
            'backgroundColor': 'Teal',
            'fontWeight': 'bold',
            'font-family': "Times New Roman,Times,serif",
        },
        style_cell={'textAlign': 'Center', 'overflow': 'hidden',
                    'fontSize': 12,
                    'textOverflow': 'ellipsis',
                    # all three widths are needed
                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                    'whiteSpace': 'normal',
                    'background': 'white',
                    'padding': '10px',
                    'font-family': "Times New Roman,Times,serif",

                    },

        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'lineHeight': '15px',
            'fontSize': 12,
            'textOverflow': 'ellipsis',
            'padding': '5px',
            'font-family': "Times New Roman,Times,serif",

        },
    ), ]),
    html.Div(
        [html.Label(["INDICATORS SUMMARY"],
                    style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", }), ]),
    dbc.Row([
        dbc.Col([card]), dbc.Col([card1]), dbc.Col([card2]), dbc.Col([card3]), dbc.Col([card4]), dbc.Col([card5]),
        dbc.Col([card6])
    ]),
    html.Div(
        [html.Label(["GENERAL OUTPATIENT DEPARTMENT MONTHLY PERFORMANCE"],
                    style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", }),
         dcc.Graph(
             id='GOPD-graph',
             figure=fig
         ), ]),

    html.Label(["CHILD WELFARE CLINIC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='CWC-graph',
        figure=fig1
    ),
    html.Label(["ANTENATAL CARE CLINIC  MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='ANC-graph',
        figure=fig2
    ),
    html.Label(["POSTNATAL CARE CLINIC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='PNC-graph',
        figure=fig3
    ),
    html.Label(["FAMILY PLANNING CLINIC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='FP-graph',
        figure=fig4
    ),
    html.Label(["DELIVERIES MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='Deliveries-graph',
        figure=fig5
    ),

]),


##################################################################################################

main_page = dbc.Container([layout],fluid = True)
