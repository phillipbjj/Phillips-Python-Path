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


# Define the list of possibilities
#possibleMoves = [1, 2, 3]

possibleMoves = ["R", "P", "S"]
rounds = 3
def rockPaperScissorsGame(possibleMoves, rounds):
    if rounds == 0:
        return [[]]
    else:
        subset2 = rockPaperScissorsGame(possibleMoves, rounds - 1)
        return [[move] + subset1 for move in possibleMoves for subset1 in subset2]

for sequence in rockPaperScissorsGame(possibleMoves, rounds):
    print(sequence)

    