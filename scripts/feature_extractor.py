from matplotlib import pyplot as plt
import numpy as np


from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import accuracy_score
from scripts.data_processor import DataProcessor
from sklearn import preprocessing
import pandas as pd



class FeatureExtractor:

    def __init__(self):

        pass

    def get_data (self):
        self.train_data =DataProcessor.read_csv("processeddata.csv")
        #print(self.train_data.head())
        return self.train_data

    def prepare_data(self, df):
        #Filtering of values having 0 in state holiday
        df = df[df.StateHoliday != 0]
        #Filtering of values having 0 in state holiday
        df = df[df.StateHoliday != 0]
        label=df["Sales"]
        #df=df.drop(["Sales"],axis=1)
        df['CompetitionDistance']=pd.to_numeric(df['CompetitionDistance'],errors='coerce').fillna(0, downcast='infer')
        #len = 22
        return df
    def correct_feature(data):
        encoder = preprocessing.LabelEncoder()
        data['StoreType']=encoder.fit_transform(data['StoreType'])
        data['Assortment']=encoder.fit_transform(data['Assortment'])
        data['PromoInterval']=encoder.fit_transform(data['PromoInterval'])
        data['StateHoliday']=encoder.fit_transform(data['StateHoliday'])
        #print(len(data))
        return data
    
    def trimm_correlated(df_in, threshold):
        df_corr = df_in.corr(method='pearson', min_periods=1)
        df_not_correlated = ~(df_corr.mask(np.tril(np.ones([len(df_corr)]*2, dtype=bool))).abs() > threshold).any()
        un_corr_idx = df_not_correlated.loc[df_not_correlated[df_not_correlated.index] == True].index
        df_out = df_in[un_corr_idx]
        return df_out
    def select_feature_corr (df):
        df= FeatureExtractor.trimm_correlated(df,0.75)
        return df
    def select_feature_mutual ( df,label):
        Y= label
        X=df
        importance=mutual_info_classif(X,Y)
        feature_importance=pd.Series(importance, dataframe.columns[0:len(dataframe.columns)-1])
        feature_importance.plot(kind='barh', color='teal')
        plt.show
        mutual_data=df[['Customers','StoreType','CompetitionDistance',
        'Store','Promo','Promo2SinceWeek','CompetitionOpenSinceYear','Assortment',
        'CompetitionOpenSinceMonth','DayOfWeek','Sales']]
        return mutual_data

    
    def check_features(self):
        row_data = FeatureExtractor.get_data(self)
        data= FeatureExtractor.prepare_data(self,row_data)
        label=data["Sales"]
        df=data.drop(["Sales"],axis=1)
        data = FeatureExtractor.correct_feature(df)
        selected_data = FeatureExtractor.select_feature_corr(df)
        mutual = FeatureExtractor.select_feature_mutual(df,label)
        print (len(mutual.columns))
        print (len(selected_data.columns))
        return selected_data


       

        
        


 










if __name__ == "__main__":
    featureobj= FeatureExtractor()
    featureobj.check_features()














