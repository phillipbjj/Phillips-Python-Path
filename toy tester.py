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

def rockPaperScissorsGame(moves, rounds):
    if rounds != 0:
        for lol in range(len(moves)):
            for result in rockPaperScissorsGame(moves[lol:], rounds - 1):
                yield [moves[lol]] + result
    else:
        yield []

moves = ["R", "P", "S",]  # list of moves
rounds = 3  # number of rounds

for combination in rockPaperScissorsGame(moves, rounds):
    print(combination)