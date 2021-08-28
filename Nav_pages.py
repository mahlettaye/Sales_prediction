import sys
sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/')
import streamlit as st 

from pages import data_viz_II
from pages import data_viz
from pages import prediction



#Navigation to the pages 
PAGES={
    
    "Data Visualization": data_viz,
    "Data Visualization II": data_viz_II,
    "Prediction":prediction
} 



def main():
    
    st.sidebar.title("MENU")
    


    st.write("""
    # Rosemann Sales Prediction App
    Rossmann is one of the largest drug store chains in Europe with around 56,200 employees and more than 4000 stores across Europe.
    In 2019 Rossmann had more than €10 billion turnover in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.
    

    """)
    

    
    selection = st.sidebar.selectbox("Select....",list(PAGES.keys()))

    page= PAGES[selection]

    with st.spinner(f"Loading {selection}..."):
        page.app()


if __name__=="__main__":
    main()