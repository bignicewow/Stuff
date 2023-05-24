import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute("INSERT INTO students VALUES (6, 'Igor', 17, 9.9),(7, 'Reginald', 18, 0.4)")

conn.commit()

conn.close()