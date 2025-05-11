import sqlite3
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
# for i in questions.questions.keys():
#     if len(i) == 2:
#         print(i[1])
#     else:
#         print(i[1:])


# questions = [(1, 'a', 'Problem-solving / analytical thinking'), 
#              (1, 'b', 'Communication'), (1, 'c', 'Creativity and innovation'), 
#              (1, 'd', 'Leadership'), (1, 'e', 'Adaptability'), 
#              (1, 'f', 'Something else'), (2, 'a', 'Coding'), 
#              (2, 'b', 'Designing'), (2, 'c', 'Analyzing data'), 
#              (2, 'd', 'Ensuring systems run smoothly'), (2, 'e', 'Leading projects'), 
#              (3, 'a', 'Psychology'), (3, 'b', 'Maths'), (3, 'c', 'Marketing'), (3, 'd', 'Art'), 
#              (3, 'e', 'Management'), (3, 'f', 'Computing'), 
#              (4, 'a', 'Keeping the project organized, handling potential risks, and keeping everyone updated'), 
#              (4, 'b', "Creating the company's visual identity and design elements"), 
#              (4, 'c', 'Finding ways the business can grow and improve'), 
#              (4, 'd', 'Designing and launching campaigns to increase brand visibility'), 
#              (4, 'e', 'Taking care of all the behind-the-scenes technology'), 
#              (4, 'f', 'Understanding customers and making sure their needs are met'), 
#              (5, 'a', 'Leader'), (5, 'b', 'Organizer'), (5, 'c', 'Idea generator'), 
#              (5, 'd', 'Listener'), (5, 'e', 'Other'), 
#              (6, 'a', "That it's been thoroughly tested by potential users"), (6, 'b', 'That the interface is intuitive and helps users stay motivated and engaged'), (6, 'c', 'That development stays on schedule and within the planned budget'), (6, 'd', 'That the app runs smoothly without any glitches'), (6, 'e', "That there's a strong marketing plan to reach the target audience"), (6, 'f', 'That the design is visually appealing and aligns with the brand identity'), (6, 'g', 'That it meets an unmet need in the current market'), (7, 'a', 'I plan everything in detail and stick to my schedule'), (7, 'b', 'I start with tasks I really enjoy'), (7, 'c', 'I rely on deadlines and reminders to keep me on track'), (7, 'd', 'I often work best under pressure, even if it means last-minute pushes'), (7, 'e', 'I combine a solid plan with flexibility when needed'), (8, 'a', 'I like working alone on focused tasks'), (8, 'b', 'I enjoy working with others as a team'), (8, 'c', 'I like leading and organizing people'), (8, 'd', 'I enjoy learning and tackling new challenges'), (9, 'a', 'I want to become a top technical expert in my field'), (9, 'b', 'I aim to take on leadership roles and guide teams or projects'), (9, 'c', 'I value a stable job that supports a strong work-life balance'), (9, 'd', 'I strive to constantly innovate and embrace new challenges'), (10, 'a', 'No, not at all'), (10, 'b', "I don't think so"), (10, 'c', "I'm unsure"), (10, 'd', 'I think so'), (10, 'e', 'Definitely')]
# cursor.executemany("INSERT INTO options(question_id,option_key,text) VALUES (?,?,?)",questions)
connection.commit()
connection.close()