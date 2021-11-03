import pandas as pd
import streamlit as st
import numpy as np
import folium
import plotly.express as px

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from datetime import datetime

#Expandir layout
st.set_page_config(layout='wide')

#decorador para ler o arquivo da memória em vez do disco
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

def drop_rows(data):
    data = data.drop(data[data['bathrooms'] == 0].index)

    return data

def reset_index(data):
    data = data.reset_index(drop=True)

    return data

def conversion_date(data):
    # conversion of date
    data['date'] = pd.to_datetime(data['date'])

    return data

def set_feature(data):
    # add new features
    data['price_m2'] = (data['price'] / data['sqft_lot']) * 0.093

    return data

def overview_data(data):
    st.title("House Rocket company by Lucas Quemelli")
    st.title("Data Overview")

    st.sidebar.title("Data overview filters")
    # filtro para coluna
    f_attributes = st.sidebar.multiselect('Enter columns', data.columns)

    # filtro para região
    f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].unique())

    # attributes + zipcode = selecionar colunas e linhas
    # attributes = selecionar colunas
    # zipcode = selecionar linhas
    # 0 + 0 = retorno o dataset original

    if (f_zipcode != []) & (f_attributes != []):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), :]

    elif (f_zipcode == []) & (f_attributes != []):
        data = data.loc[:, f_attributes]

    else:
        data = data.copy()

    st.dataframe(data)

    c1, c2 = st.columns((1, 1))

    # Average metrics
    df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # Merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    df.columns = ['Zipcode', 'Total Houses', 'Price', 'Sqft Living', 'Price/m2']

    c1.header('Values for zipcode')
    c1.dataframe(df, height=600, width=400)

    # Descriptive statistics
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))

    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    df1 = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()

    df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

    c2.header('Descriptive analysis')
    c2.dataframe(df1, height=600, width=400)

    return None

def portfolio_density(data):
    st.title('Region Overview')

    c1, c2 = st.columns((1, 1))
    c1.header('Portfolio density')

    df = data.sample(10)

    # Base Map - Folium
    density_map = folium.Map(location=[data['lat'].mean(),
                                       data['long'].mean()],
                             default_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(density_map)

    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold R${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}'.format(
                          row['price'],
                          row['date'],
                          row['sqft_living'],
                          row['bedrooms'],
                          row['bathrooms'],
                          row['yr_built'])).add_to(marker_cluster)

    with c1:
        folium_static(density_map)

    return None

def commercial_distribution(data):
    st.sidebar.title('Commercial attributes filters')
    st.title('Commercial Attributes')

    # -----Average Price per Year
    # filters
    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())

    st.sidebar.subheader('Select max construction year')
    f_year_built = st.sidebar.slider('Year Built', min_year_built,
                                     max_year_built,
                                     max_year_built)

    st.header('Price per year')

    # data selection
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['price', 'yr_built']].groupby('yr_built').mean().reset_index()

    # plot
    fig = px.line(df, x='yr_built', y='price')
    fig.update_traces(line=dict(color='black'))
    fig.update_layout(title="Average price per construction year")
    fig.update_xaxes(title="Construction year (-)")
    fig.update_yaxes(title="Price (USD)")
    st.plotly_chart(fig, use_container_width=True)

    # -----Average Price per Day
    st.header('Price per date of purchase')
    st.sidebar.subheader('Select max date')

    # load data
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # filters
    min_date = datetime.strptime((data['date'].min()), '%Y-%m-%d')
    max_date = datetime.strptime((data['date'].max()), '%Y-%m-%d')

    f_date = st.sidebar.slider('Date', min_date, max_date, max_date)

    # data selection
    data['date'] = pd.to_datetime(data['date'])
    df = data.loc[data['date'] < f_date]
    df = df[['price', 'date']].groupby('date').mean().reset_index()

    # plot
    fig = px.line(df, x='date', y='price')
    fig.update_traces(line=dict(color='black'))
    fig.update_layout(title="Average price per date")
    fig.update_xaxes(title="Date (Month YEAR)")
    fig.update_yaxes(title="Price (USD)")
    st.plotly_chart(fig, use_container_width=True)

    # ------Histograma

    st.header('Price distribution')
    st.sidebar.subheader('Select max price')

    # filters
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    # data selection
    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)
    df = data.loc[data['price'] < f_price]

    # plot
    fig = px.histogram(df, x='price', nbins=50, color_discrete_sequence=['black'])
    fig.update_layout(title="Number of properties per price")
    fig.update_xaxes(title="Price (USD)")
    fig.update_yaxes(title="Absolute frequency (-)")
    st.plotly_chart(fig, use_container_width=True)

    return None

def attributes_distribution(data):
    st.sidebar.title('Properties attributes filters')
    st.title('Properties Attributes')

    # filters
    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms',
                                      sorted(set(data['bedrooms'].unique())))

    f_bathrooms = st.sidebar.selectbox('Max number of bathrooms',
                                       sorted(set(data['bathrooms'].unique())))

    c1, c2 = st.columns(2)

    # House per bedrooms
    c1.header('Properties per bedrooms')
    df = data[data['bedrooms'] <= f_bedrooms]
    fig = px.histogram(df, x='bedrooms', nbins=19,color_discrete_sequence=['black'])
    fig.update_layout(title="Number of properties per bedrooms")
    fig.update_xaxes(title="Number of bedrooms (-)")
    fig.update_yaxes(title="Absolute frequency (-)")
    c1.plotly_chart(fig, use_container_width=True)

    # House per bathrooms
    c2.header('Properties per bathrooms')
    df = data[data['bathrooms'] <= f_bathrooms]
    fig = px.histogram(df, x='bathrooms', nbins=19,color_discrete_sequence=['black'])
    fig.update_layout(title="Number of properties per bathrooms")
    fig.update_xaxes(title="Number of bathrooms (-)")
    fig.update_yaxes(title="Absolute frequency (-)")
    c2.plotly_chart(fig, use_container_width=True)

    # filters
    f_floors = st.sidebar.selectbox('Max number of floors',
                                    sorted(set(data['floors'].unique())))

    st.sidebar.subheader("Select waterfront")
    f_waterview = st.sidebar.checkbox('Only properties with waterfront')

    c1, c2 = st.columns(2)

    # House per floors
    c1.header('Properties per floors')
    df = data[data['floors'] <= f_floors]
    fig = px.histogram(df, x='floors', nbins=19,color_discrete_sequence=['black'])
    fig.update_layout(title="Number of properties per floors")
    fig.update_xaxes(title="Number of floors (-)")
    fig.update_yaxes(title="Absolute frequency (-)")
    c1.plotly_chart(fig, use_container_width=True)

    # House per waterview
    if f_waterview:
        df = data[data['waterfront'] == 1]

    else:
        df = data.copy()

    c2.header('Properties per waterfront')
    fig = px.histogram(df, x='waterfront', nbins=10,color_discrete_sequence=['black'])
    fig.update_layout(title="Number of properties per waterfront")
    fig.update_xaxes(title="Waterfront¹ (-)")
    fig.update_yaxes(title="Absolute frequency (-)")
    c2.plotly_chart(fig, use_container_width=True)

    st.subheader("¹On the chart 'properties per waterfront', 1 means waterfront and 0 means no waterfront.")

    return None

if __name__ == '__main__':

    path = "kc_house_data.csv"
    data = get_data(path)

    data = drop_rows(data)

    data = reset_index(data)

    data = conversion_date(data)

    data = set_feature(data)

    overview_data(data)

    portfolio_density(data)

    commercial_distribution(data)

    attributes_distribution(data)

