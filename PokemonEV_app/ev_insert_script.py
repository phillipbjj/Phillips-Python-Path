import csv

"""with open('Pokedex_EVs.txt', 'r') as file:
    lines = file.readlines()

with open('Pokedex_EVs.txt', 'w') as file:
    for line in lines:
        if ',0,0,0,0,0,0' not in line:
            line = line.strip() + ',0,0,0,0,0,0\n'
        file.write(line)"""
        
"""with open('Pokedex_EVs.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
with open('Pokedex_EVs.csv', 'w') as file:
    for row in data:
        row[0] = row[0].replace('#', '')
        file.write(line)
        
        ##0001 Bulbasaur,0,0,1,0,0,0,1"""
        
        
with open('Pokedex_EVs.csv', 'r') as f:
    lines = f.readlines()

with open('Pokedex_EVs.csv', 'w') as f:
    for line in lines:
        f.write(line.replace(' ', ','))