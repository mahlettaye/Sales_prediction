
from numpy.core.numeric import NaN
from scripts.feature_extractor import FeatureExtractor
import unittest
import pandas as pd

class TestSum(unittest.TestCase):
    """
		A class for unit-testing class for feature_extractor.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""
    
    def test_correct_feature_normal_args(self):
        """
        The Function that tests correct_feature function in data_processor.py 

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
        result = FeatureExtractor.correct_feature(df)
        actual = df['StoreType'].dtypes
      
        expected = "int64"
        self.assertEqual(actual, expected, "unmatch data type ") 
    
    def test_correct_feature_bad_args(self):
        """
        The Function that tests correct_feature function in data_processor.py 

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
        1270.0,9,2008,0,1,1900,"Jan,Nov,Jul,Oct"]
             


        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result = FeatureExtractor.correct_feature(df)
        actual = df['PromoInterval'].dtypes
      
        expected = "int64"
        self.assertEqual(actual, expected, "unmatch data type ") 

    def test_correct_feature_bad_args_coustomer(self):
        """
        The Function that tests correct_feature function in data_processor.py 

        Parameters
        ----------
        df: pd.Dataframe : woth string value for customer column 
        

        Returns
        -------
        df: pd.Dataframe :

        """
        # Create a list of lists where each inner list is a row of the DataFrame
        data_list = [1,'a','2015-07-31',
        5263,555,1,1,0,1,'Jul',31,2015,31,'c','a',
        1270.0,9,2008,0,1,1900,"Jan,Nov,Jul,Oct"]
             


        df = pd.DataFrame(data=[data_list], columns=['Store','DayOfWeek','Date',
        'Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday',
        'Month','Day','Year','Week','StoreType','Assortment',
        'CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
        'Promo2SinceYear','PromoInterval'
                 ])
        result = FeatureExtractor.correct_feature(df)
        actual = df['Customers'].dtypes
      
        expected = "int64"
        self.assertEqual(actual, expected, "unmatch data type ") 
    
    
    

    



if __name__ == '__main__':
    # to run test terminal python3 -m unittest discover -v -s . -p "*Test_*.py"
    unittest.main()