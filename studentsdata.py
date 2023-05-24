import sqlite3

def select_students_by_grade(grade):

    conn = sqlite3.connect('mydatabase.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE grade >= ?",(grade,))

    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")

    conn.close()

select_students_by_grade(0.4)