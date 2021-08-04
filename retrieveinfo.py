import sqlite3

connection = sqlite3.connect("Details.db")
cursor = connection.cursor()
details = cursor.execute("SELECT * FROM VICTIMS")
print(details.fetchall())