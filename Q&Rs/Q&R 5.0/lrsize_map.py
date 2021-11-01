import pandas as pd
import streamlit as st
import plotly.express as px

#Expand layout
st.set_page_config(layout='wide')

#read file from memory
@st.cache(allow_output_mutation=True)

def get_data(path):
    data = pd.read_csv(path)

    return data

def question_ten(data):
    st.title("House Rocket real estate company by Lucas Quemelli")

    houses = data[['id','lat','long','sqft_living','price']]

    fig = px.scatter_mapbox(houses,
                            lat = 'lat',
                            lon = 'long',
                            size = 'sqft_living',
                            hover_data = ['price'],
                            color_continuous_scale = px.colors.cyclical.IceFire,
                            size_max = 15,
                            zoom = 10)

    fig.update_layout(mapbox_style = 'open-street-map',
                      height = 600,
                      margin = {'r':0, 'l':0, 't': 0, 'b': 0})

    st.header("House Rocket's property map - property size proportional to the living room")
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == '__main__':
    path = "new_data.csv"
    data = get_data(path)

    question_ten(data)