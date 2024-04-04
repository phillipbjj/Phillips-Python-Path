import csv

# Read the data from the file
with open('Pokedex_EVs.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Add a total column
for row in data:
    Total = sum(int(i) for i in row[1:])  # Sum the numbers in the row
    row.append(Total)  # Append the total to the row

# Write the data back to the file
with open('Pokedex_EVs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)