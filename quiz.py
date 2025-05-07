import modules.questions as Questions
import modules.scoring as Scoring
import modules.roles as Roles
questions = Questions.questions 
scores = Scoring.scores
user_input = {
    "Q"+str(i):None for i in range(1,len(questions))                
}   #recording what the user selects in a dictionary to match the scores dictionary structure
for i,j in questions.items(): #Printing out the questions
    print("\n"+i,end=" ")
    for j1,j2 in j.items():
        print(j1+"\n")
        for j3,j4 in j2.items():
            print(j3+" "+j4)
        question_input = input("Answer: ") #Please enter a valid input so it can work :)
        user_input[i]=question_input #score is collected here
roles = Roles.roles
total_score = { #A dictionary creation for the total score for each role
    role:0 for role in roles
}
sorted_scores = sorted(total_score.values(),reverse=True)
for i,j in user_input.items(): #Loop to traverse the users inputs matching it with the Questions' scores
    if j in scores[i].keys():
        for j1,j2 in scores[i][j].items():
            total_score[j1] += j2   #This will give the score for each role
result = None
highest = 0
for i,j in total_score.items():
    if j>highest:
        highest=j
        result=i
#Print out quiz result
print("\n")
for i,j in total_score.items():
    print(i," ",j)
print("\nQuiz result: ",result)