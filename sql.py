import sqlite3
connection = sqlite3.connect("questions.db")
cursor = connection.cursor()
questions = [(1, 'Q1', 'Which skill do you think is your strongest?'),
             (2, 'Q2', 'Which of the following appeals to you the most?'), 
             (3, 'Q3', 'If you had to take a class right now, which would you pick?'), 
             (4, 'Q4', "You're teaming up with a few friends to launch a small business. Which role do you think you'd contribute to the most?"), 
             (5, 'Q5', 'When you work in a group, which role do you tend to take on?'), 
             (6, 'Q6', "You're getting ready to launch a brand new fitness app. What matters most to you?"), 
             (7, 'Q7', 'How do you manage your time and prioritise tasks?'), 
             (8, 'Q8', 'Which best describes how you like to work?'), 
             (9, 'Q9', 'What best describes your long-term career vision?'), 
             (10, 'Q10', "I'm good at prioritising tasks when I'm working on multiple projects")]
#Tables: questions (id("1"),key("Q1"...),text) questions added
cursor.execute("SELECT key,text FROM questions")
for i in cursor.fetchall():
    print(f"{i[0]} {i[1]}")
connection.commit()
connection.close()