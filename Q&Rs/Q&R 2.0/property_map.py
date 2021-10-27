import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

#read file from memory
@st.cache(allow_output_mutation=True)

def get_data(path):
   data = pd.read_csv(path)

   return data

def question_five(data):
   st.title("House Rocket real estate company by Lucas Quemelli")

   st.header("Data overview")
   st.dataframe(data)

   data_map = data[['id', 'lat', 'long', 'price']]
   fig_map = px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id', hover_data=['price'], zoom=3,
                               height=300)

   fig_map.update_layout(mapbox_style='open-street-map', height=600, margin={"r": 0, "l": 0, "t": 0, "b": 0})

   st.header("House Rocket's property map")
   st.plotly_chart(fig_map, use_container_width=True)

   return None

if __name__ == '__main__':
   path = "new_data.csv"
   data = get_data(path)

   question_five(data)