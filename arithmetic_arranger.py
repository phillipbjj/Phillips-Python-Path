
mathProblems = ["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"]
#mathProblems = ["150 + 50", "107 + 1337", "123 + 1", "36 - 24"]
variableCheck = any(problemStr.isalpha() for problem in mathProblems for problemStr in problem)

def arithmetic_arranger(mathProblems, showAnswers = False):

    for equation in mathProblems:    
        mathStr_long = [mathStr for mathStr in equation.split() if mathStr not in ['+', '-']]
        for mathStr_short in mathStr_long:
            if len(mathStr_short) > 4:
                return "Error: Numbers cannot be more than four digits"
            
    if len(mathProblems) > 5:       
        return "Error: Too many problems."
    
    elif any("*" in mathProb or "/" in mathProb for mathProb in mathProblems):
        return "Error: Operator must be '+' or '-'."
    
    elif variableCheck == True:     
        return "Error: Numbers must only contain digits."
    
    else:
        mathProblem_1 = mathProblems[0].split()
        mathProblem_2 = mathProblems[1].split()
        mathProblem_3 = mathProblems[2].split()
        mathProblem_4 = mathProblems[3].split()
        
        if showAnswers:
            answer_1 = []
            answer_2 = []
            answer_3 = []
            answer_4 = []
            problemsAndAnswers = [(mathProblem_1, answer_1), (mathProblem_2, answer_2), (mathProblem_3, answer_3), (mathProblem_4, answer_4)]
            for probs, answers in problemsAndAnswers:#[mathProblem_1, mathProblem_2, mathProblem_3, mathProblem_4]:
                if probs == '+':
                    answer = mathProblem_1[1] + mathProblem_1[2]
                elif probs == '-':
                    answer = int(1) - int(2)
                answers.append(answer)
                
        return print(mathProblem_1[0].rjust(6), "  ",  mathProblem_2[0].rjust(6), "  ",  mathProblem_3[0].rjust(6), "  ",  mathProblem_4[0].rjust(6), '\n' + 
                    mathProblem_1[1], mathProblem_1[2].rjust(4), "  ", mathProblem_2[1], mathProblem_2[2].rjust(4), "  ",
                    mathProblem_3[1], mathProblem_3[2].rjust(4), "  ", mathProblem_4[1], mathProblem_4[2].rjust(4) +  
                    '\n' "------","  ","------","  ","------","  ","------"), '\n'

    
              
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



