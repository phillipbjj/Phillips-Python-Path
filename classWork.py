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
    def __init__(self, rank, age, weight, height):
        self.rank = rank
        self.age = age
        self.weight = weight
        self.height = height
    def __str__(self):
        return f'Rank: {self.rank}, Age: {self.age}, Weight: {self.weight} lbs, Height: {self.height} in'

#Create instances for each athlete   
athlete1 = bjjFighter('Blue', 26, 175, 68)
athlete2 = bjjFighter('Blue', 22, 180, 73)

tournamentSignups = {}
#Add the athletes to the dictionary

tournamentSignups['Phillip Dempsey'] = athlete1
tournamentSignups['Jack Howell'] = athlete2

print(tournamentSignups['Phillip Dempsey'])     
print(tournamentSignups['Jack Howell'])    