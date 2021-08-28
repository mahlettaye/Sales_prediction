import streamlit as st
import pandas as pd
#import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/')

st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    
    #with st.spinner("Loading"):
    #Header
    st.write("""### Data Exploration results""")
        


    #Reading the data
    training_sample_subset=pd.read_csv("data/RF_train.csv")


    #display the data as a table
    st.write(training_sample_subset.head(20))


    #header
    st.write("Distribution of Orders (Dependent variable)")


    #bar plot
    #temp=training_sample_subset["ordered"].value_counts()
    fig, ax = plt.subplots()
    #To know when are the stores open and store type
    ax = sns.countplot(x='Sales', hue='StoreType', data=training_sample_subset[:100], palette='Set1')
    #ax.bar(["Not ordered","Ordered"],temp,color ='maroon',width = 0.4)
    #plt.xlabel("Order status")
    #plt.ylabel("No. of customers")
    st.pyplot()


  

    




