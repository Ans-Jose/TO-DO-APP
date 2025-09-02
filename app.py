from flask import Flask, render_template, request, jsonify, session
import sqlite3, os, uuid

app = Flask(__name__)
app.secret_key = os.urandom(24) 

def get_db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.before_request
def assign_session():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())  # generate a unique ID


# ---- Home / To-Do List ----
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks WHERE user_id = ?", (session['user_id'],)).fetchall()
    conn.close()
    return jsonify([dict(t) for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (task, date, time, user_id) VALUES (?, ?, ?, ?)",
        (data['task'], data['date'], data['time'], session['user_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added!"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    result = conn.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, session['user_id'])
    )
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Deleted successfully!"})


# ---- Past Records ----
@app.route('/past')
def past():
    return render_template('past.html')

@app.route('/past_records', methods=['GET'])
def past_records():
    conn = get_db_connection()
    records = conn.execute("SELECT * FROM past_tasks WHERE user_id = ?", (session['user_id'],)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in records])

@app.route('/past_records', methods=['POST'])
def add_past_record():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO past_tasks (task, status, user_id) VALUES (?, ?, ?)",
        (data['entry'], data['status'], session['user_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Past record added!"})

@app.route('/past_records/<int:id>', methods=['DELETE'])
def delete_past_record(id):
    conn = get_db_connection()
    result = conn.execute(
        "DELETE FROM past_tasks WHERE id = ? AND user_id = ?", (id, session['user_id'])
    )
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        return jsonify({"error": "Record not found"}), 404
    return jsonify({"message": "Deleted successfully!"})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=True)
