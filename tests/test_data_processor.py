
from numpy.core.numeric import NaN
from scripts.data_processor import DataProcessor
import unittest
import pandas as pd

class TestSum(unittest.TestCase):
    """
		A class for unit-testing function in the data_processor.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""
    
    def test_Find_null_normal_args(self):
        """
        The Function that tests Find_null function in data_processor.py 

        Parameters
        ----------
        df: pd.Dataframe :
        

        Returns
        -------
        df: pd.Dataframe :

        """
        # Create a list of lists where each inner list is a row of the DataFrame
        data_list = [1,5,'2015-07-31',
        5263,555,1,1,0,1,'Jul',31,2015,31,'c','a',
        1270.0,9,2008,0,1,1900,"Jan,Apr,Jul,Oct"]
             


        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result = DataProcessor.Find_null_(df)
        actual = len(df.columns)
        expected = 22
        self.assertEqual(actual, expected, "result is not dataframe") 
    
    
    

    def test_handdle_missing_values(self):
        

        data_list = [1,5,'2015-07-31',
        5263,555,1,1,0,1,'Jul',31,2015,31,'c','a',
        1270.0,9,2008,0,1,1900,"Jan,Apr,Jul,Oct"]

        data_list1 = [478,6,'2014-07-05',4741,495,
        1,0,0,0,'Jul',5,2014,27,'d','c',1940.0,3,2012,
        0,1,1900,"Jan,Apr,Jul,Oct"]
        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        df1 = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result, result1 = DataProcessor.handdle_missing_values(df,df1)
        actual = result.isnull().values.any()
        actual1 = result1.isnull().values.any()
        expected = False
        
        self.assertEqual(actual, expected, "Your input contains unexpectednull value")
        self.assertEqual(actual1, expected, "Your input contains unexpected null value")


    

    def test_handdle_missing_values_bad_args(self):
        
        "tesing with missing value for Promo2SinceYear"
        data_list = [1,5,'2015-07-31',
        5263,555,1,1,0,1,'Jul',31,2015,31,'c','a',
        1270.0,9,2008,0,1,NaN,"Jan,Apr,Jul,Oct"]

        data_list1 = [478,6,'2014-07-05',4741,495,
        1,0,0,0,'Jul',5,2014,27,'d','c',1940.0,3,2012,
        0,1,NaN,"Jan,Apr,Jul,Oct"]
        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        df1 = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result, result1 = DataProcessor.handdle_missing_values(df,df1)
        actual = result.isnull().values.any()
        actual1 = result1.isnull().values.any()
        expected = False
        
        self.assertEqual(actual, expected, "Your input contains unexpectednull value")
        self.assertEqual(actual1, expected, "Your input contains unexpected null value")
    
    def test_handdle_missing_values_bad_args1(self):
            
        "tesing with missing value for Promo2SinceYear"
        data_list = [1,5,'2015-07-31',
        5263,555,1,1,0,1,'Jul',31,2015,31,'c','a',
        1270.0,NaN,2008,0,1,1900,"Jan,Apr,Jul,Oct"]

        data_list1 = [478,6,'2014-07-05',4741,495,
        1,0,0,0,'Jul',5,2014,27,'d','c',1940.0,NaN,2012,
        0,1,1900,"Jan,Apr,Jul,Oct"]
        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        df1 = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result, result1 = DataProcessor.handdle_missing_values(df,df1)
        actual = result.isnull().values.any()
        actual1 = result1.isnull().values.any()
        expected = False
        
        self.assertEqual(actual, expected, "Your input contains unexpected null value")
        self.assertEqual(actual1, expected, "Your input contains unexpected null value")



if __name__ == '__main__':
    # to run test terminal python3 -m unittest discover -v -s . -p "*Test_*.py"
    unittest.main()