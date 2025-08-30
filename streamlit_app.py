import streamlit as st
import pandas as pd

st.title("ML App - Mertali Tercan")

st.info("Welcome")

with st.expander('Data:'):
  st.write("**Raw data**")
  data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  data

  st.write('**X**')
  X = data.drop(['species'], axis=1)
  X

  st.write('**Y**')
  y = data['species']
  y

