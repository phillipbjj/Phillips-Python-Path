with open('pokemonimages.txt', 'w') as f:
    f.write('pokemonimages.txt = {\n')
    for i in range(1, 650):
        f.write(f"    '#{str(i).zfill(4)}': '{i}.png',\n")
    f.write('}\n')