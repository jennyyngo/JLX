import unittest
from parse_csv import read_data
import csv

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'street_food_vendors.csv'

    def test_csv_read_data_headers(self):
        self.assertEqual(
            read_data(self.data)[0],
            ['KEY', 'LAT', 'LON', 'VENDOR_TYPE', 'STATUS', 'BUSINESS_NAME', 'LOCATION', 'DESCRIPTION']
            )

    def test_csv_read_data_key(self):
        # Expected to pass 
        self.assertEqual(read_data(self.data)[1][0], 'EB04')
        # Expected failure
        self.assertEqual(read_data(self.data)[1][2], 'EB04') 

    def test_csv_read_data_status(self):
        self.assertEqual(read_data(self.data)[1][4], 'open')
        self.assertEqual(read_data(self.data)[1][4], 'close')


if __name__ == '__main__':
    unittest.main()

data = "street_food_vendors.csv"
read_data(data)