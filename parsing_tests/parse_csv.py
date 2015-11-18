import csv


def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


# ---- run code ---- #

data = "street_food_vendors.csv"
read_data(data)