
mathProblems = ["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"]
variableCheck = any(problem.isalpha() for problem in mathProblems)
def arithmetic_arranger(mathProblems):
    if len(mathProblems) > 5:
        return "Error: Too many problems."
    elif any("*" in mathProb or "/" in mathProb for mathProb in mathProblems):
        return "Error: Operator must be '+' or '-'."
    elif variableCheck == True:
        return "Error: Numbers must only contain digits."
    else:
        for prob in mathProblems:
            if len(mathProblems[prob]) > 4:
                return "Error: Numbers cannot be more than four digits"
    #else:
    return print(mathProblems[0], mathProblems[1], mathProblems[2], mathProblems[3])
        #for problem in mathProblems[0:]:

arithmetic_arranger(mathProblems)
        
        
    
quit() 
print(mathProblems[0], mathProblems[1], mathProblems[2], mathProblems[3]) 
#print(" ",mathProblems[0],"  ",mathProblems[1],"  ",mathProblems[2],"  ",mathProblems[3])
stop = 4
#print()
strippedProblems = mathProblems[0].split()
print(strippedProblems[0].rjust(6))
print(strippedProblems[1], strippedProblems[2].rjust(6))
print("------","","------","","------","","------")



