with open('Pokedex_EVs.txt', 'r') as file:
    lines = file.readlines()

with open('Pokedex_EVs.txt', 'w') as file:
    for line in lines:
        if ',0,0,0,0,0,0' not in line:
            line = line.strip() + ',0,0,0,0,0,0\n'
        file.write(line)