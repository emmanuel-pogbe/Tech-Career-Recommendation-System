questions = {
    "Q1":{
        "Which skill do you think is your strongest?": {
            "a":"Problem-solving / analytical thinking",
            "b":"Communication",
            "c":"Creativity and innovation",
            "d":"Leadership",
            "e":"Adaptability",
            "f":"Something else"
        }
    },
    "Q2": {
        "Which of the following appeals to you the most?": {
            "a":"Coding",
            "b":"Designing",
            "c":"Analyzing data",
            "d":"Ensuring systems run smoothly",
            "e":"Leading projects"
        }
    },
    "Q3":{
        "If you had to take a class right now, which would you pick?":{
            "a":"Psychology",
            "b":"Maths",
            "c":"Marketing",
            "d":"Art",
            "e":"Management",
            "f":"Computing"
        }
    },
    "Q4":{
        "You're teaming up with a few friends to launch a small business. Which role do you think you'd contribute to the most?":{
            "a":"Keeping the project organized, handling potential risks, and keeping everyone updated",
            "b":"Creating the company's visual identity and design elements",
            "c":"Finding ways the business can grow and improve",
            "d":"Designing and launching campaigns to increase brand visibility",
            "e":"Taking care of all the behind-the-scenes technology",
            "f":"Understanding customers and making sure their needs are met"
        }
    },
    "Q5":{
       "When you work in a group, which role do you tend to take on?": {
            "a":"Leader",
            "b":"Organizer",
            "c":"Idea generator",
            "d":"Listener",
            "e":"Other"
       }
    },
    "Q6":{
        "You're getting ready to launch a brand new fitness app. What matters most to you?": {
            "a":"That it's been thoroughly tested by potential users",
            "b":"That the interface is intuitive and helps users stay motivated and engaged",
            "c":"That development stays on schedule and within the planned budget",
            "d":"That the app runs smoothly without any glitches",
            "e":"That there's a strong marketing plan to reach the target audience",
            "f":"That the design is visually appealing and aligns with the brand identity",
            "g":"That it meets an unmet need in the current market"
        }     
    },
    "Q7":{
        "How do you manage your time and prioritise tasks?": {
            "a":"I plan everything in detail and stick to my schedule",
            "b":"I start with tasks I really enjoy",
            "c":"I rely on deadlines and reminders to keep me on track",
            "d":"I often work best under pressure, even if it means last-minute pushes",
            "e":"I combine a solid plan with flexibility when needed"
        }
    },
    "Q8":{
        "Which best describes how you like to work?":{
            "a":"I like working alone on focused tasks",
            "b":"I enjoy working with others as a team",
            "c":"I like leading and organizing people",
            "d":"I enjoy learning and tackling new challenges"
        }
    },
    "Q9": {
        "What best describes your long-term career vision?": {
            "a":"I want to become a top technical expert in my field",
            "b":"I aim to take on leadership roles and guide teams or projects",
            "c":"I value a stable job that supports a strong work-life balance",
            "d":"I strive to constantly innovate and embrace new challenges"
        }
    },
    "Q10": {
       "I'm good at prioritising tasks when I'm working on multiple projects": {
            "a":"No, not at all",
            "b":"I don't think so",
            "c":"I'm unsure",
            "d":"I think so",
            "e":"Definitely"
        }
    }
}
# id = [i for i in range(1,len(questions)+1)]
# key = [i for i in questions.keys()]
# text = []
# the_tuple = []
# for i,j in questions.items():
#     for j1,_ in j.items():
#         text.append(j1)
# for i in range(len(id)):
#     the_tuple.append((id[i],key[i],text[i]))
# questions__ = []
# for i,j in questions.items():
#         question_id = int(i[1:])
#         for j1,j2 in j.items():
#             for j3,j4 in j2.items():
#                 option_key = j3
#                 text = j4
#                 questions__.append((question_id,option_key,text))