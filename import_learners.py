import sqlite3
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'learners.db')
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data', 'grade10.csv')

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learners (
            admission_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            gender TEXT, grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

def import_csv_to_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT OR REPLACE INTO learners (admission_no, name, gender, grade)
                VALUES (?, ?, ?, ?)
            ''', (row['admission_no'], row['name'], '', 'Grade 10'))
    
    conn.commit()
    conn.close()
    print("CSV data imported successfully.")

if __name__ == '__main__':
    create_tables()
    import_csv_to_db()
