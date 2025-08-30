import streamlit as st
import pandas as pd
import numpy as np

st.title("Machine Learning Application - Mertali Tercan")
st.info("Hello!")

data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

for animal in data:
  animal.body_mass_g = animal.body_mass_g / 1000

data.rename(columns={'body_mass_g' : 'body_mass_kg'}, inplace='True')

with st.expander('Data:'):
  st.write("**Raw data**")
  data

  st.write('**X**')
  X = data.drop('species', axis=1)
  X

  st.write('**Y**')
  y = data.species
  y

with st.expander('Visualize:'):
  st.scatter_chart(data=data, x='bill_depth_mm', x_label='Bill Depth', y='body_mass_g', y_label='Body Mass', color='species')

