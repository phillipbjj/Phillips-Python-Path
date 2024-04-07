from PokemonEV_reader import load_data

pokemon_data = load_data('Pokedex_EVs.csv')
print(pokemon_data[0].__dict__)
#print(pokemon_data("Charmander"))