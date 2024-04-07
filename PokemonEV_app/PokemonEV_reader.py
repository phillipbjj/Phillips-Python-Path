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
        data = [Pokemon(*row) for row in reader]
        #This line returns the list of Pokemon objects.
    return data

pokemon_data = load_data('Pokedex_EVs.csv')
#used for serializing (pickling) and deserializing (unpickling) Python objects.
"""import pickle

def save_data_to_file(data, filename):
    #This line opens the file with the given filename in binary write mode ('wb')
    with open(filename, 'wb') as file:
        #This line uses the pickle.dump function to write the pickled representation of data (in this case, the list of Pokemon objects) to the file.
        pickle.dump(data, file) 
def load_data_from_file(filename):
    #This line opens the file with the given filename in binary read mode ('rb').
    with open(filename, 'rb') as file:
        #This line uses the pickle.load function to read the pickled data from the file and return it. The returned data will be a list of Pokemon objects.
        return pickle.load(file) 

pokemon_data = load_data('Pokedex_EVs.csv')
save_data_to_file(pokemon_data, 'pokedex_pokemon.pkl')

pokemon_data = load_data_from_file('pokedex_pokemon.pkl')
"""