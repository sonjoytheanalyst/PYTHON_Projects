import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px 


#import dataset
st.title("Implementation of Plotly and Steeamlit for making map")
df = px.data.gapminder()
st.write(df.head())

st.write(df.columns)

# Summary Test
st.write(df.describe())

# data management
year_option = df['year'].unique().tolist()
year = st.selectbox("Which Year Should we Plot?", year_option,0)

#df = df[df['year']==year]

# Ploting

fig = px.scatter(df, x ='gdpPercap', y ='lifeExp',size='pop',color='country',hover_name='country',
                 log_x=True,size_max=55,range_x=[100,1000000],range_y=[20,90],
                 animation_frame='year', animation_group='country')
st.write(fig)

