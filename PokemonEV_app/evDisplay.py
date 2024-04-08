from PokemonEV_reader import pokemon_data

def evDisplay(pokemon_data, pokemon_name):
    if pokemon_name in pokemon_data:
        pokemonObject = pokemon_data[pokemon_name]
        print(f"{pokemon_name}:")
        for attribute, value in pokemonObject.__dict__.items():
            if attribute != 'total' and value.isdigit() and int(value) > 0:
                print(f"{attribute}: {value}")
    else:
        print(f"No data available for {pokemon_name}")
        
#evDisplay(pokemon_data, 'Venusaur')