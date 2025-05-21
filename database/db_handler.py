import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'learners.db')

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learners (
            admission_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            gender TEXT,
            grade TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admission_no TEXT,
            subject TEXT,
            score INTEGER,
            FOREIGN KEY(admission_no) REFERENCES learners(admission_no)
        )
    ''')
    conn.commit()
    conn.close()

def get_learners_by_grade(grade):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT admission_no, name FROM learners WHERE grade = ?", (grade,))
    results = cursor.fetchall()
    conn.close()
    return results

def save_mark(admission_no, subject, score):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO marks (admission_no, subject, score) VALUES (?, ?, ?)",
                   (admission_no, subject, score))
    conn.commit()
    conn.close()
