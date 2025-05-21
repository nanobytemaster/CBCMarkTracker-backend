from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'learners.db')

@app.route('/submit_marks', methods=['POST'])
def submit_marks():
    data = request.json
    admission_no = data.get('admission_no')
    subject = data.get('subject')
    marks = data.get('marks')
    if not all([admission_no, subject, marks]):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO marks (admission_no, subject, marks)
        VALUES (?, ?, ?)
    ''', (admission_no, subject, marks))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'Marks submitted successfully'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
