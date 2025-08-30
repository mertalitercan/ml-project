import streamlit as st
import pandas as pd

st.title("ML App - Mertali Tercan")

st.info("Welcome")

with st.expander('Data:'):
  st.write("**Raw data**")
  data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  data

  st.write('**X**')
  X = data.drop('species', axis=1)
  X

  st.write('**Y**')
  y = data.species
  y

st.markdown('hey')
st.markdown('hey')

with st.expander('Visualize the data:'):
  st.scatter_chart(data=data, x='bill_depth_mm', x_label='Bill Depth', y='body_mass_g', y_label='Body Mass', color='species')

