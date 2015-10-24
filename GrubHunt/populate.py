import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpsc310_project.settings')

import django
django.setup()

from GrubHunt.models import FoodVendor
#used for parsing lat and lon
from decimal import Decimal
import csv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'static/data/street_food_vendors.csv')

class DatabasePopulater():

    def add_vendor(self, values):
        v, created = FoodVendor.objects.get_or_create(key=values[0])
        v.key=values[0]
        v.latitude=values[1]
        v.longitude=values[2]
        v.vendorType=values[3]
        v.open=values[4]
        v.businessName=values[5]
        v.address=values[6]
        v.description=values[7]
        v.save()
        return created

    def parseLine(self, row):
	    #imput is KEY,LAT,LON,VENDOR_TYPE,STATUS,BUSINESS_NAME,LOCATION,DESCRIPTION
        #values = line.split(',')
        row[1] = Decimal(row[1])
        row[2] = Decimal(row[2])
        if(row[4] == 'open'):
            row[4] = True 
        else:
            row[4] = False
        return row

    def populate(self):
    
        createdVendors = []
        with open(DATA_FILE, "r") as myfile:
            reader = csv.reader(myfile)
            next(reader, None)  # skip the headers
            for row in reader:
                values = self.parseLine(row)
                created = self.add_vendor(values)
                if created:
            	    createdVendors.append(values[0])

        return createdVendors