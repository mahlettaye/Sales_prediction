import streamlit as st
import pandas as pd



def app():

    with st.spinner("Loading"):
        gender = st.sidebar.selectbox('gender',('Male','Female'))
        def user_input_features():
            gender = st.sidebar.selectbox('gender',('Male','Female'))

            PaymentMethod = st.sidebar.selectbox('PaymentMethod',('Bank transfer (automatic)', 'Credit card (automatic)', 'Mailed check', 'Electronic check'))

            data = {'gender':[gender], 
            'PaymentMethod':[PaymentMethod]
            }
            features = pd.DataFrame(data)

            return features
  

    




