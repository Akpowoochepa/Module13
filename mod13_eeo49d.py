import unittest
from StockTime import get_time_series_option, get_start_date, get_end_date, get_start_time
import datetime
from unittest.mock import patch
from ping import pingAPI
from RenderGraph import render_graph

#Unit Test Classes
class TimeTest(unittest.TestCase):
    # Time series Test
    def test_time_series_option(self):
        result = get_time_series_option()
        self.assertIn(result, {1})

    def test_time_series_option1(self):
        result = get_time_series_option()
        self.assertEqual(result, 2)

    def test_time_series_option2(self):
        result = get_time_series_option()
        self.assertEqual(result, 3)

    def test_time_series_option3(self):
        result = get_time_series_option()
        self.assertEqual(result, 4)

    # Start_Date Test
    def test_get_start_date(self):
        result = get_start_date()
        self.assertIsInstance(result, datetime.datetime)

    # End_date Test
    def test_get_end_date(self):
        start_date = datetime.datetime.strptime('2020-01-24', '%Y-%m-%d')
        result = get_end_date(start_date=start_date)
        self.assertIsInstance(result, datetime.datetime)
        self.assertGreaterEqual(result, start_date)

    # Start_time Test
    def test_get_start_time(self):
        result = get_start_time()
        self.assertIsInstance(result, datetime.time)

#API ping test
class PingApiTest(unittest.TestCase):
    def test_pingapi(self):
        csv_data = "timestamp,open,high,low,close,volume\n2020-06-24,50,20,1,4,1000\n2020-07-20,20,25,10,22,2000\n2020-07-24,30,35,20,32,4000"

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = csv_data.encode('utf-8')

        lower_date = datetime.datetime.strptime('2020-06-24', '%Y-%m-%d')
        upper_date = datetime.datetime.strptime('2020-07-24', '%Y-%m-%d')

        try:
            result = pingAPI(func=1, symbol='IBM', lowerDate=lower_date, upperDate=upper_date)
        
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

        self.assertEqual(len(result), 1) 

    def test_pingapi1(self):
        csv_data = "timestamp,open,high,low,close,volume\n2020-06-24,50,20,1,4,1000\n2020-07-20,20,25,10,22,2000\n2020-07-24,30,35,20,32,3000"

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = csv_data.encode('utf-8')

        lower_date = datetime.datetime.strptime('2020-06-24', '%Y-%m-%d')
        upper_date = datetime.datetime.strptime('2020-07-24', '%Y-%m-%d')

        try:
            result = pingAPI(func=2, symbol='IBM', lowerDate=lower_date, upperDate=upper_date)
        
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

        self.assertEqual(len(result), 1) 

    
    def test_pingapi2(self):
        csv_data = "timestamp,open,high,low,close,volume\n2020-06-24,50,20,1,4,1000\n2020-07-20,20,25,10,22,2000\n2020-07-24,30,35,20,32,2000"

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = csv_data.encode('utf-8')

        lower_date = datetime.datetime.strptime('2020-06-24', '%Y-%m-%d')
        upper_date = datetime.datetime.strptime('2020-07-24', '%Y-%m-%d')

        try:
            result = pingAPI(func=3, symbol='IBM', lowerDate=lower_date, upperDate=upper_date)
        
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

        self.assertEqual(len(result), 6) 


    
    def test_pingapi3(self):
        csv_data = "timestamp,open,high,low,close,volume\n2020-06-30,30,20,1,4,1000\n2020-07-31,20,25,10,22,2000"

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = csv_data.encode('utf-8')

        lower_date = datetime.datetime.strptime('2020-06-24', '%Y-%m-%d')
        upper_date = datetime.datetime.strptime('2020-07-24', '%Y-%m-%d')

        try:
            result = pingAPI(func=4, symbol='IBM', lowerDate=lower_date, upperDate=upper_date)
        
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

        self.assertEqual(len(result), 2) 

#Testing the Charts
class TestGraph(unittest.TestCase):
    def test_Graph_test(self):
        test_data = [
            ["timestamp", "open", "high", "low", "close", "volume"],
            ["2020-05-25", "100.0", "105.0", "95.0", "120.0", "20000"],
            ["2020-05-26", "102.0", "110.0", "100.0", "145.0", "40000"]
        ]
        try:
            render_graph(chart_type= 1, start_date_str='2020-05-24', end_date_str='2020-06-24', data=test_data, stock_symbol='IBM')
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_Graph_test2(self):
        test_data = [
            ["timestamp", "open", "high", "low", "close", "volume"],
            ["2020-05-25", "200.0", "305.0", "100.0", "120.0", "20000"],
            ["2020-05-26", "207.0", "310.0", "150.0", "245.0", "40000"]
        ]
        try:
            render_graph(chart_type= 1, start_date_str='2020-05-24', end_date_str='2020-06-24', data=test_data, stock_symbol='IBM')
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


if __name__ == '__main__':
    unittest.main()