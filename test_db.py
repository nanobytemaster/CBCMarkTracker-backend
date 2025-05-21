from database import db_handler

def add_dummy_learners():
    import sqlite3
    conn = sqlite3.connect('data/learners.db')
    cursor = conn.cursor()

    # Add some dummy learners if not already in the table
    learners = [
        ('ADM001', 'Alice W.', 'F', 'Grade 7'),
        ('ADM002', 'Bob K.', 'M', 'Grade 7'),
        ('ADM003', 'Cathy M.', 'F', 'Grade 8')
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO learners (admission_no, name, gender, grade)
        VALUES (?, ?, ?, ?)
    ''', learners)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_handler.create_tables()
    add_dummy_learners()
    print("Tables created and dummy data added successfully!")
