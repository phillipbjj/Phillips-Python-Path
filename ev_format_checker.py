import re

# Regular expression pattern for "string,int,int,int,int,int,int"
pattern = r'^[a-zA-Z\s]+,\d+,\d+,\d+,\d+,\d+,\d+$'

with open('Pokedex_EVs.txt', 'r') as file:
    for line in file:
        if not re.match(pattern, line.strip()):
            print(f'Invalid format: {line}')