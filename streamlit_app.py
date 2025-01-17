import streamlit as st
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 

# loading the saved models

diabetes_model = pickle.load(open('/Users/joad/Desktop/ML model/Diabetes/python code/Diabetes prediction system/Saved model/diabetes_model.rfc', 'rb'))

def clear_text():
  st.session_state["1"] = ""
  st.session_state["2"] = ""
  st.session_state["3"] = ""
  st.session_state["4"] = ""
  st.session_state["5"] = ""
  st.session_state["6"] = ""
  st.session_state["7"] = ""
  st.session_state["8"] = ""

# sidebar for navigation

with st.sidebar: 
    
    selected = option_menu('Diabetes Disease Prediction System',
                           ['Diabetes Prediction'],
                            
                           icons = ['hospital'],
                           
                           default_index = 0)
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    st.title('Diabetes Prediction using ML')
    
    Pregnancies = st.text_input('Number of Pregnancies', key='1')
    Glucose = st.text_input('Glucose Level', key='2')
    BloodPressure = st.text_input('Blood Pressure Value', key='3')
    SkinThickness = st.text_input('Skin Thickness Value', key='4')
    Insulin = st.text_input('Insulin Level', key='5')
    BMI = st.text_input('BMI Value', key='6')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', key='7')
    Age = st.text_input('Age of the Person', key='8')
    
    col1, col2 = st.columns(2)  # Create two columns

    with col1:  
        submit_button = st.button("Submit") 
     
    with col2:  
        clear_button = st.button("Clear Form", on_click=clear_text) 
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    #creating a button for Prediction
    #if st.button('Submit'):
    if submit_button:
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is diabetic'
            
        else:
            diab_diagnosis = 'The person is not diabetic'
            
    if clear_button:

        Pregnancies = ""  
        Glucose = "" 
        BloodPressure = ""  
        SkinThickness = "" 
        Insulin = ""  
        BMI = "" 
        DiabetesPedigreeFunction = ""  
        Age = "" 
            
    st.success(diab_diagnosis)
    


