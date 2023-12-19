
mathProblems = ["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"]
def arithmetic_arranger(mathProblems):
    if len(mathProblems) > 5:
        return "Too many problems"
    elif any("*" in mathProblems or "/" in mathProblems for problem in mathProblems):
        return "Only addition or subtraction"
    else:
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



