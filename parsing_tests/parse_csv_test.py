import unittest
from parse_csv import read_data
import csv

#run tests by typing python parse_csv_test.py -v in terminal


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

# checks first entry's key is correct
    def test_csv_read_data_key(self):
        # Expected to pass 
        self.assertEqual(read_data(self.data)[1][0], 'EB04')

# checks random entries of KEY are not empty
    def test_csv_read_data_vendortype(self):
        self.assertNotEqual(read_data(self.data)[5][0], "")
        self.assertNotEqual(read_data(self.data)[35][0], "")
        self.assertNotEqual(read_data(self.data)[70][0], "")

# checks first entry's status is correct
    def test_csv_read_data_status(self):
        self.assertEqual(read_data(self.data)[1][4], 'open')

# checks random entries since all entries' VENDOR_TYPE should be 'vendor_food'
    def test_csv_read_data_vendortype(self):
        self.assertEqual(read_data(self.data)[5][3], 'vendor_food')
        self.assertEqual(read_data(self.data)[40][3], 'vendor_food')
        self.assertEqual(read_data(self.data)[60][3], 'vendor_food')

# checks random entries of VENDOR_TYPE are not empty
    def test_csv_read_data_vendortype(self):
        self.assertNotEqual(read_data(self.data)[5][3], "")
        self.assertNotEqual(read_data(self.data)[40][3], "")
        self.assertNotEqual(read_data(self.data)[60][3], "")

# checks first entry's business name is an empty string
    def test_csv_read_data_businessname(self):
        self.assertEqual(read_data(self.data)[1][5], "")

#checks another entry's business name is NOT an empty string
    def test_csv_read_data_businessname(self):
        self.assertEqual(read_data(self.data)[51][5], "Japadog")

#checks first entry's description is correct
    def test_csv_read_data_description(self):
        self.assertEqual(read_data(self.data)[1][7], 'Hot Dogs')

#checks that lat can never be empty 
    def test_csv_read_data_lat(self):
        self.assertNotEqual(read_data(self.data)[1][1], "")
        self.assertNotEqual(read_data(self.data)[25][1], "")
        self.assertNotEqual(read_data(self.data)[43][1], "")

#checks that lon can never be empty 
    def test_csv_read_data_lon(self):
        self.assertNotEqual(read_data(self.data)[1][2], "")
        self.assertNotEqual(read_data(self.data)[54][2], "")
        self.assertNotEqual(read_data(self.data)[71][2], "")

if __name__ == '__main__':
    unittest.main()

data = "street_food_vendors.csv"
read_data(data)