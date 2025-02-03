import streamlit as st
import pickle
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    with open('/Users/joad/Desktop/ML model/Diabetes/python code/Diabetes prediction system/Saved model/diabetes_model.rfc', "rb") as f:
        return pickle.load(f)

model = load_model()

# Streamlit UI
st.title("AI Model Deployment on Streamlit Cloud")

input_data = st.number_input("Enter a number:")
if st.button("Predict"):
    prediction = model.predict(np.array([[input_data]]))
    st.write(f"Prediction: {prediction[0]}")
