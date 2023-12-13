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

def rockPaperScissorsGame(rps_moves, rounds):
    if rounds != 0:
        for move in range(len(rps_moves)):
            for outcome in rockPaperScissorsGame(rps_moves[move:], rounds - 1):
                yield [rps_moves[move]] + outcome
    else:
        yield []
            

rps_moves = ["R", "P", "S"]
rounds = 3

for options in rockPaperScissorsGame(rps_moves, rounds):
    print(options)