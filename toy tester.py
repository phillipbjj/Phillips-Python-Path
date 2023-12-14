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

def generate_combinations(options, rounds):
    if rounds == 0:
        return [[]]
    else:
        smaller_combinations = generate_combinations(options, rounds - 1)
        return [[option] + combination for option in options for combination in smaller_combinations]

options = ["R", "P", "S"]
rounds = 3

for combination in generate_combinations(options, rounds):
    print(combination)