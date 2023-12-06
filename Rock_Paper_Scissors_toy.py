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

outcome = []
rounds = 3  # number of rounds
choice = "R"  #first choice
while rounds > 0:
    rounds = rounds - 1

    #def rockPaperScissors(choice):
    if choice == "R":
        outcome.append("R")
    elif choice == "P":
        outcome.append("P")
    elif choice == "S":
        outcome.append("S")
            #elif choice == "R" or choice == "P" or choice == "S":
                #rockPaperScissors()
    else:
        outcome.append("Not a choice")
clean_outcome = ''.join(outcome)
print(clean_outcome)



def rockPaperScissors(choice):
    if choice == "R":
        outcome.append("R")
        
    elif choice == "P":
        outcome.append("P")
        
    elif choice == "S":
        outcome.append("S")
        
            #elif choice == "R" or choice == "P" or choice == "S":
                #rockPaperScissors()

print(outcome)
print(outcome2)
print(outcome3)











