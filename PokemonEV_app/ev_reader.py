import csv
from pokemonevs import Pokemon

def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [Pokemon(*row) for row in reader]
    return data