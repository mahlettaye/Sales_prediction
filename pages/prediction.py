import streamlit as st
import joblib
import pandas as pd

import sys
sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/')



def read_csv (filename):
    
        try:
            data= pd.read_csv(filename)
        
        except FileNotFoundError as e:
            print("unable to open")
        
        return data

def load(model_path):
   
    model = joblib.load(model_path)
    return model

def inference(model, df):
    df=df.drop(['Unnamed: 0'], axis=1)
    df=df[['Customers','StoreType','CompetitionDistance','Store','Promo','Promo2SinceWeek']]
        #df = pd.DataFrame([row], columns = feat_cols)

    #X = scaler.transform(df)
        #features = pd.DataFrame(X)
    prediction=model.predict(df)
    return prediction
            
       

   

def app ():

    with st.spinner("Loading"):
        test_file= st.file_uploader('Upload File', type=['csv'])

        if (test_file):
            test=read_csv(test_file)
            st.dataframe(test.head(20))
            sample=test[:5]
            if (st.button('Predict')):
                model = load('Xmodel.joblib')
                result = inference(model, sample)
               
                st.dataframe(result)
            
   

