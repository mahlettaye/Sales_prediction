import sys
sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/')
import streamlit as st 

from pages import index
from pages import data_viz
from pages import prediction



#Navigation to the pages 
PAGES={
    
    "Data Visualization": data_viz,
    "Prediction":prediction
} 



def main():
    
    st.sidebar.title("MENU")


    st.write("""
    # Churn Prediction App

    Customer churn is defined as the loss of customers after a certain period of time. Companies are interested in targeting customers

    who are likely to churn. They can target these customers with special deals and promotions to influence them to stay with

    the company. 

    This app predicts the probability of a customer churning using Telco Customer data. Here

    customer churn means the customer does not make another purchase after a period of time. 

    """)
    #gender = st.sidebar.selectbox('gender',('Male','Female'))

    
    selection = st.sidebar.selectbox("Select....",list(PAGES.keys()))

    page= PAGES[selection]

    with st.spinner(f"Loading {selection}..."):
        page.app()


if __name__=="__main__":
    main()