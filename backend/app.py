from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Frontend ile bağlantı kurmamızı sağlar

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

# Veritabanı ve tablo oluşturma
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/requests', methods=['GET'])
def get_requests():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, title, description, status FROM requests")
    rows = c.fetchall()
    conn.close()

    requests = []
    for row in rows:
        requests.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "status": row[3]
        })
    return jsonify(requests)

@app.route('/api/requests', methods=['POST'])
def create_request():
    data = request.get_json()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO requests (title, description) VALUES (?, ?)",
              (data.get("title"), data.get("description")))
    conn.commit()
    conn.close()
    return jsonify({"message": "Request added."}), 201

@app.route('/api/requests/<int:request_id>', methods=['PUT'])
def update_status(request_id):
    data = request.get_json()
    new_status = data.get("status", "pending")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE requests SET status = ? WHERE id = ?", (new_status, request_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Status updated."})

if __name__ == '__main__':
    app.run(debug=True)