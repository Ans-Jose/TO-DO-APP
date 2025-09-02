from flask import Flask, render_template, request, jsonify, session
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"  # needed for sessions

@app.route('/')
def home():
    # initialize a tasks list for this user if it doesn't exist
    if 'tasks' not in session:
        session['tasks'] = []
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(session.get('tasks', []))

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_data = {
        "task": data['task'],
        "date": data['date'],
        "time": data['time']
    }
    tasks = session.get('tasks', [])
    tasks.append(task_data)
    session['tasks'] = tasks
    return jsonify({"message": "Task added!"}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = session.get('tasks', [])
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        session['tasks'] = tasks
        return jsonify({"message": "Task deleted!"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
