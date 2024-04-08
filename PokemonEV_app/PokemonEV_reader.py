import csv
#This line imports the Pokemon class from the pokemonevs module. This class is used to create Pokemon objects.
from pokemonevs import Pokemon 
#This line defines a function called load_data that takes one argument: filename.
#This function is used to load data from a CSV file.
def load_data(filename):
    #This line opens the file with the name filename in read mode ('r'). 
    #The with statement ensures that the file is properly closed after it is no longer needed.
    with open(filename, 'r') as file:
        #This line creates a reader object that can iterate over lines in the specified CSV file.
        reader = csv.reader(file)
        #This line uses a list comprehension to create a list of Pokemon objects.
        # For each row in the CSV file, it creates a Pokemon object with the values in the row.
        # The * operator is used to unpack the values from each row.
        data = {row[0]: Pokemon(*row) for row in reader}
        #This line returns the list of Pokemon objects.
    return data

pokemon_data = load_data('Pokedex_EVs.csv')