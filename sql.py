import sqlite3
import modules.questions as questions
connection = sqlite3.connect("quizinfo.db")
cursor = connection.cursor()
# questions = [(1, 'Q1', 'Which skill do you think is your strongest?'),
#              (2, 'Q2', 'Which of the following appeals to you the most?'), 
#              (3, 'Q3', 'If you had to take a class right now, which would you pick?'), 
#              (4, 'Q4', "You're teaming up with a few friends to launch a small business. Which role do you think you'd contribute to the most?"), 
#              (5, 'Q5', 'When you work in a group, which role do you tend to take on?'), 
#              (6, 'Q6', "You're getting ready to launch a brand new fitness app. What matters most to you?"), 
#              (7, 'Q7', 'How do you manage your time and prioritise tasks?'), 
#              (8, 'Q8', 'Which best describes how you like to work?'), 
#              (9, 'Q9', 'What best describes your long-term career vision?'), 
#              (10, 'Q10', "I'm good at prioritising tasks when I'm working on multiple projects")]
#Tables: questions (id("1"),key("Q1"...),text) questions added
roles_ = [(1, 'Backend Developer'), (2, 'Cloud Engineer'), 
          (3, 'Cybersecurity Specialist'), (4, 'Data Analyst'), 
          (5, 'Data Scientist'), (6, 'DevOps Engineer'), 
          (7, 'Frontend Developer'), (8, 'Full-Stack Developer'), 
          (9, 'Machine Learning Engineer'), (10, 'Mobile App Developer'),
          (11, 'Product Manager'), (12, 'Project Manager'), (13, 'UI/UX Designer')]
# cursor.execute("CREATE TABLE roles (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)")
# # print("Success!")
# cursor.executemany("INSERT INTO roles VALUES (?,?)",roles_)
# cursor.execute("SELECT * FROM roles")

# cursor.execute("""CREATE TABLE options (
#                id INTEGER PRIMARY KEY,
#                question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
#                option_key TEXT NOT NULL,
#                text TEXT NOT NULL,
#                UNIQUE(question_id,option_key)
#                )
# """)
for i in questions.questions.keys():
    if len(i) == 2:
        print(i[1])
    else:
        print(i[1:])
# cursor.executemany("INSERT INTO options(question_id,option_key,text) VALUES (?,?,?)")
connection.commit()
connection.close()