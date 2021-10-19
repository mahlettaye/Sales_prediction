from matplotlib.pyplot import get
from data_processor import DataProcessor
import calendar


class DataCleaner :
    """
    
    """
    def __init__(self) -> None:
        self.train_filename = "/home/mahlet/Desktop/Sales_prediction/data/train.csv"
        self.test_filename = "/home/mahlet/Desktop/Sales_prediction/data/train.csv"
        self.store_filename = "/home/mahlet/Desktop/Sales_prediction/data/store.csv"
        self.train_data = DataProcessor.read_csv(self.train_filename)
        self.test_data = DataProcessor.read_csv(self.test_filename)
        self.store_data = DataProcessor.read_csv(self.store_filename)

        
    def get_data(df1,df2,df3):
        df_train,df_test= DataProcessor.change_date(df1,df2)
        
        train_df = DataProcessor.merge(df_train, df3, 'Store')
        test_df = DataProcessor.merge(df_test, df3, 'Store')
        
        return train_df,test_df
    def process_df (df1,df2):
        train_df = DataProcessor.drop_cols(df1)
        test_df = DataProcessor.drop_cols(df2)
        train_df,test_df = DataProcessor.handdle_missing_values(train_df,test_df)
        
        return train_df,test_df

    def month_convertor (self):
        train_df,test_df = DataCleaner.get_data(self.train_data,self.test_data,self.store_data)
        train_df,test_df = DataCleaner.process_df(train_df, test_df)
        train_df['Month'] =  train_df['Month'].apply(lambda x: calendar.month_abbr[x])
        #print (train_df['Month'])
        return train_df,test_df
        



if __name__ == "__main__":
    datacleanerobj = DataCleaner()
    datacleanerobj.month_convertor()