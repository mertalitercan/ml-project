import streamlit as st
import pandas as pd

st.title("ML App - Mertali Tercan")

st.info("Welcome")

data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
data

