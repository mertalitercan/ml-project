import streamlit as st
import pandas as pd
import numpy as np
import math

st.title("Machine Learning Application - Mertali Tercan")
st.info("Hello!")

data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

data['body_mass_g'] /= 1000

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
  st.scatter_chart(data=data, x='bill_depth_mm', x_label='Bill Depth (mm)', y='body_mass_kg', y_label='Body Mass (kg)', color='species')

with st.sidebar:
  st.header('Your inputs:')
  island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream'), placeholder='Choose island...')
  gender = st.selectbox('Gender', ('Male', 'Female'), placeholder='Choose gender...')
  bill_length_mm = st.slider('Bill Length (mm)', min(data['bill_length_mm'], max(data['bill_length_mm'], mean(data['bill_length_mm']

