import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import calendar



def app():
    
    #with st.spinner("Loading"):
    #Header
    st.write("""### Data Exploration results II""")
        


    #Reading the data
    training_sample_subset=pd.read_csv("data/RF_train.csv")


    #display the data as a table
    st.write(training_sample_subset.head(20))


    #header
    st.write("Distribution of Orders (Dependent variable)")


    
    # select all stores that were open
    store_a= training_sample_subset[training_sample_subset['StoreType']=="a"]
    subs = store_a[store_a['Open']!=0 ]

    # groupby Year and Month
    selected_sales = subs.groupby(['Year', 'Month'])['Sales'].median()
    

    # plot
    fig, (axis1) = plt.subplots(1,1, figsize=(10,7))
    selected_sales.unstack().T.plot(ax=axis1)   
    tmp = axis1.set_title("Store A sales in a year each month")
    tmp = axis1.set_ylabel("Sales")
    tmp = axis1.set_xticks(range(0,13))
    tmp = axis1.set_xticklabels(calendar.month_abbr)
   
    st.pyplot()


    




