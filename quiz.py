import modules.scoring as Scoring
import sqlite3

connection = sqlite3.connect("quizinfo.db")
cursor = connection.cursor()
cursor.execute("SELECT key,text FROM questions")
question_headings = cursor.fetchall() 
scores = Scoring.scores
def get_roles(cursor):
    cursor.execute("SELECT name FROM roles")
    roles_from_db = cursor.fetchall()
    roles = []
    for role in roles_from_db:
        roles.append(role[0])
    return roles
def get_options(cursor,question_id):
    cursor.execute("SELECT option_key,text FROM options WHERE question_id = ?",(question_id,))
    return cursor.fetchall()
def display_question(question_id, question_text, cursor):
    print(f"\n{question_id} {question_text}")
    question_id_format = int(question_id[1:])
    options = get_options(cursor, question_id_format)
    valid_keys = []
    for opt_key, opt_text in options:
        print(f"{opt_key} {opt_text}")
        valid_keys.append(opt_key)
    return valid_keys
user_input = {
    "Q"+str(i):None for i in range(1,len(question_headings))                
}   #recording what the user selects in a dictionary to match the scores dictionary structure
for question_id,question_text in question_headings:
    valid_keys = display_question(question_id,question_text,cursor)
    while True:
        question_input = input("Answer: ")
        if question_input in valid_keys:
            break
        print("Input invalid, Please Try again: ",end=" ")
    user_input[question_id]=question_input #score is collected here
roles = get_roles(cursor)
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