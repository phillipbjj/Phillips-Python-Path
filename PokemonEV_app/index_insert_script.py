with open('Pokedex_EVs.csv', 'r') as file:
    lines = file.readlines()
#Adds index
"""with open('Pokedex_EVs.csv', 'w') as file:   
    for i, line in enumerate(lines, start=1):
        # Add the index number to the start of the line
        line = f"#{i:04d} {line}"
        file.write(line)"""
#Adds index at line to remove duplicate and extra index#       
with open('Pokedex_EVs.csv', 'w') as file:      
    for i, line in enumerate(lines, start=1):
        # If the line number is X or greater, add the index number to the start of the line
        if i >= 627:    #line
            _, rest_of_line = line.split(maxsplit=1)
            line = f"#{i-24:04d} {rest_of_line}" #line -# = actual index {i-8:04d}
        file.write(line)