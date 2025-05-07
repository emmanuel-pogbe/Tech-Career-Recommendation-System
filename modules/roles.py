import sqlite3
connection = sqlite3.connect("quizinfo.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM roles")
role_tuple = cursor.fetchall()
roles = [i[0] for i in role_tuple]
connection.commit()
connection.close()
if __name__ == "__main__":
    print(len(roles))