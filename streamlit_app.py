import streamlit as st
import pandas as pd

st.file_uploader('http://127.0.0.1:8000/diabetes_prediction')
pd.read('http://127.0.0.1:8000/diabetes_prediction')
