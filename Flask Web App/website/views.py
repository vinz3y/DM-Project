from flask import Blueprint, render_template, url_for
import pandas as pd 
import json
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objs as go


#defien that this file is a blueprint of the application
#set name of blueprint as views
views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prices/btc')
def btc():
    
    df = px.data.medals_wide()
    fig1 = px.line(df, x="nation", y=['nation', 'gold', 'silver', 'bronze'], title="Wide=Form Input")
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    testPlt = create_plot()

    return render_template("currencies/btc.html" , title="BTC Price", graphJSON=graphJSON , testPlt= testPlt )


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@views.route('/testplot')
def test():
    data = [
        ("01-01-2022", 19997),
        ("02-01-2022", 197),
        ("03-01-2022", 2997),
        ("04-01-2022", 997)
    ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]