import csv

# Read the data from the file
with open('Pokedex_EVs.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Remove the '#' from the index numbers
for row in data:
    row[5] = row[5].replace(' ', ',')

# Write the modified data back to the file
with open('Pokedex_EVs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)