def arithmetic_arranger(problems, showAnswers = False):

    #problems = ["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"]
    variableCheck = any(problemStr.isalpha() for problem in problems for problemStr in problem)
    
    for equation in problems:    
        mathStr_long = [mathStr for mathStr in equation.split() if mathStr not in ['+', '-']]
        for mathStr_short in mathStr_long:
            if len(mathStr_short) > 4:
                return "Error: Numbers cannot be more than four digits"
            
    if len(problems) > 5:       
        return "Error: Too many problems."
    
    elif any("*" in mathProb or "/" in mathProb for mathProb in problems):
        return "Error: Operator must be '+' or '-'."
    
    elif variableCheck == True:     
        return "Error: Numbers must only contain digits."
    
    else:
        mathProblem_1 = problems[0].split()
        mathProblem_2 = problems[1].split()
        mathProblem_3 = problems[2].split()
        mathProblem_4 = problems[3].split()
        
        if showAnswers:
            answer_1 = []
            answer_2 = []
            answer_3 = []
            answer_4 = []
            problemsAndAnswers = [(mathProblem_1, answer_1), (mathProblem_2, answer_2), (mathProblem_3, answer_3), (mathProblem_4, answer_4)]
            for probs, answers in problemsAndAnswers:
                if '+' in probs:
                    answer = int(probs[0]) + int(probs[2])
                    answers.append(answer)
                elif '-' in probs:
                    answer = int(probs[0]) - int(probs[2])
                    answers.append(answer)
            strAnswer_1 = [str(i) for i in answer_1] 
            strAnswer_2 = [str(i) for i in answer_2]
            strAnswer_3 = [str(i) for i in answer_3]
            strAnswer_4 = [str(i) for i in answer_4]
             
        return print(mathProblem_1[0].rjust(6), "  ",  mathProblem_2[0].rjust(6), "  ",  mathProblem_3[0].rjust(6), "  ",  mathProblem_4[0].rjust(6), '\n' + 
                    mathProblem_1[1], mathProblem_1[2].rjust(4), "  ", mathProblem_2[1], mathProblem_2[2].rjust(4), "  ",
                    mathProblem_3[1], mathProblem_3[2].rjust(4), "  ", mathProblem_4[1], mathProblem_4[2].rjust(4) +  
                    '\n' "------","  ","------","  ","------","  ","------", '\n', strAnswer_1[0].rjust(5), "  " +
                     strAnswer_2[0].rjust(7), "  ", strAnswer_3[0].rjust(6), "  ", strAnswer_4[0].rjust(6))

    
print(arithmetic_arranger(["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"], True))              
#arithmetic_arranger(problems, True)
        



