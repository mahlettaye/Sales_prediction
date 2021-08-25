import sys
import os
#sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/data/')
sys.path.append(os.path.abspath(os.path.join('..')))
import pandas as pd

class DataProcessor:
    def __init__(self, name):
        self.filename=name
    
    def read_csv (self,filename):

        try:
            self.data= pd.read_csv(filename)
        
        except FileNotFoundError as e:
            print ("unable to open")
        
        return self.data

if __name__=="__main__":
    processor=DataProcessor("../data/train.csv")
    train_data= processor.read_csv("/data/train.csv")
    print(train_data.head())