
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
    
    def test_identify_unique_value(self):
        """
        Test duplicate calculator function 
        """
        # Create a list of lists where each inner list is a row of the DataFrame
        data_list = [0,3,5350,1115,0,22,1900,2,1,2,0]
             


        df = pd.DataFrame(data=[data_list], columns=[
                  'Customers','StoreType','CompetitionDistance','Store','Promo','Promo2SinceWeek'
                  ,'CompetitionOpenSinceYear','Assortment','CompetitionOpenSinceMonth','DayOfWeek','Sales'])
        #result = DataProcessor.read_csv("processed_data.csv")
        result = DataProcessor.Find_null_(df)
        actual = len(df.columns)
        expected = 11
        self.assertEqual(actual, expected, "result is not dataframe") 
    
    

if __name__ == '__main__':
    # to run test terminal python3 -m unittest discover -v -s . -p "*Test_*.py"
    unittest.main()