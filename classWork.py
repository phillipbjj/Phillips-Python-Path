#class work
"""class bjjFighter:
    def __init__(self, height, age, weight, rank):
        self.height = height
        self.age = age
        self.weight = weight
        self.rank = rank

# Create instances for each athlete
fighter1 = bjjFighter(170, 28, 70, 'blue')
fighter2 = bjjFighter(180, 32, 80, 'purple')

# Store the instances in a list
fighters = [fighter1, fighter2]

# Or store the instances in a dictionary with fighter names as keys
fighters_dict = {'Fighter1': fighter1, 'Fighter2': fighter2}
"""
#When you’re dealing with instances of a class, you’re not incrementing a count. 
#Instead, you’re assigning a whole object (an instance of a class) to a key. 
#So, you would just use the assignment operator (=), like dictionary[key] = instance.

class bjjFighter:
    
    RANKS = {'White': 1, 'Blue': 2, 'Purple': 3, 'Brown': 4, 'Black': 5}
    def __init__(self, rank, age, weight, height):
        self.rank_value = self.RANKS[rank]
        self.rank_color = rank
        self.age = age
        self.weight = weight
        self.height = height
    def __str__(self):
        return f'Rank: {self.rank_color}, Age: {self.age}, Weight: {self.weight} lbs, Height: {self.height} in'

tournamentSignups = {}
tournamentSignups['Phillip Dempsey'] = bjjFighter('Blue', 26, 160, 68)
tournamentSignups['Jack Howell'] = bjjFighter('Blue', 22, 180, 73)
tournamentSignups['Martin Helouin'] = bjjFighter('Blue', 20, 160, 68)
tournamentSignups['Aaron Taylor'] = bjjFighter('White', 25, 255, 70)
tournamentSignups['Jayke Lebeau'] = bjjFighter('White', 26, 185, 72)
tournamentSignups['Travis Sutton'] = bjjFighter('Purple', 28, 145, 64)
tournamentSignups['Caleb Gilmore'] = bjjFighter('Brown', 28, 180, 70)
tournamentSignups['Gordan Ryan'] = bjjFighter('Black', 28, 240, 74)
tournamentSignups['Josh Mancuso'] = bjjFighter('Black', 40, 185, 68)
tournamentSignups['Steven Bransford'] = bjjFighter('Purple', 30, 210, 68)
tournamentSignups['Nick Patrick'] = bjjFighter('Purple', 28, 190, 69)
tournamentSignups['George Munoz'] = bjjFighter('Blue', 34, 160, 66)
tournamentSignups['Brian Miller'] = bjjFighter('Purple', 22, 160, 70)
tournamentSignups['Tyler Stanczak'] = bjjFighter('White', 29, 145, 72)

class tournamentOrganizer:
    
    def __init__(self, signups):
        self.signups = signups
#Create instances for each athlete  and add the athletes to the dictionary


#tournamentSignups['Phillip Dempsey'] = athlete1

#print(tournamentSignups['Phillip Dempsey'])  
#Used to print fighters names [keys] along with their values {attributes from class} 
"""for name, fighter in tournamentSignups.items():   
    print(f'{name}: {fighter}')  """

