#Write a function that generates every sequence of throws a single
#player could throw over a three-round game of rock-paper-scissors.
#Your output should look something like:
#["RRR",
# "RRP",
#"RRS",
#"RPR",
#...etc...
#]
#Extra credit:
#- Make your function return answers for any number of rounds.
#Example:
#rockPaperScissors(5); // => ['RRRRR', 'RRRRP', 'RRRRS', etc...]

#print(f"Turn {turn+1}: The number is 1") - formatted string literals

rounds = 3

# Define the list of possibilities
moves = ["R", "P", "S"]
move_Rock = "R"
move_Paper = "P"
move_Scissors = "S"
outcomes = []
#def rockPaperScissorsGame(3)
for turn in range(rounds):
    for move in moves:
        if move == "R":
            result1 = "R"
           
        elif move == "P":
            
        elif move == "S":
            




