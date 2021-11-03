import pandas as pd
import streamlit as st
import plotly.express as px

from datetime import datetime

#Expand layout
st.set_page_config(layout='wide')

#read file from memory
@st.cache(allow_output_mutation=True)

def get_data(path):
    data = pd.read_csv(path)

    return data

def question_map(data):
    st.title("House Rocket real estate company by Lucas Quemelli")

    st.header("Data overview")
    st.dataframe(data)

    houses = data[['id','lat','long','price','waterfront']].copy()

    for i in range(len(houses)):
        if (houses.loc[i, 'price'] >= 0) & (houses.loc[i, 'price'] < 321950):
            houses.loc[i, 'level'] = 0

        elif (houses.loc[i, 'price'] >= 321950) & (houses.loc[i, 'price'] < 450000):
            houses.loc[i, 'level'] = 1

        elif (houses.loc[i, 'price'] >= 450000) & (houses.loc[i, 'price'] < 645000):
            houses.loc[i, 'level'] = 2

        else:
            houses.loc[i, 'level'] = 3

    houses['level'] = houses['level'].astype(int)

    # Filters
    st.sidebar.title("Map filters")

    # -----Filter: waterfront
    st.sidebar.subheader("Select waterfront")
    f_waterview = st.sidebar.checkbox('Only properties with waterfront')

    # data selection
    if f_waterview:
        df = houses[houses['waterfront'] == 1]

    else:
        df = houses.copy()

    # -----Filter: price
    st.sidebar.subheader('Select max price')

    min_price = int(df['price'].min())
    max_price = int(df['price'].max())
    #avg_price = int(df['price'].mean())

    # data selection
    f_price = st.sidebar.slider('Price', min_price, max_price, max_price)
    df2 = df.loc[data['price'] < f_price]

    # Plot
    fig = px.scatter_mapbox(df2,
                            lat = 'lat',
                            lon = 'long',
                            color = 'level',
                            size = 'price',
                            color_continuous_scale = px.colors.cyclical.IceFire,
                            size_max = 15,
                            zoom = 10)

    fig.update_layout(mapbox_style='open-street-map',
                      height=600,
                      margin={'r': 0, 'l': 0, 't': 0, 'b': 0})

    st.header("Property map per waterfront and price")
    st.plotly_chart(fig, use_container_width=True)

    return None

def question_chart(data):
    # -----Average Price per day
    st.sidebar.title("Chart filter")
    st.header('Prices for dates of purchase')
    st.sidebar.subheader('Select max date')

    # load data
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # filters
    min_date = datetime.strptime((data['date'].min()), '%Y-%m-%d')
    max_date = datetime.strptime((data['date'].max()), '%Y-%m-%d')

    f_date = st.sidebar.slider('Date', min_date, max_date, max_date)

    # data selection
    data['date'] = pd.to_datetime(data['date'])
    df3 = data.loc[data['date'] < f_date]
    df3 = df3[['price', 'date']].groupby('date').mean().reset_index()

    # plot
    fig = px.line(df3, x='date', y='price')
    fig.update_traces(line=dict(color='black'))
    fig.update_layout(title="Average price per day")
    fig.update_xaxes(title="Date (Month YEAR)")
    fig.update_yaxes(title="Price (USD)")
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == '__main__':
    path = "new_data.csv"
    data = get_data(path)

    question_map(data)

    question_chart(data)