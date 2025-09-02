from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# temporary storage (list in memory)
tasks = []

# show the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# return all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_data = {
        "task": data['task'],
        "date": data['date'],
        "time": data['time']
    }
    tasks.append(task_data)
    return jsonify({"message": "Task added!"}), 201

# delete a task by index
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        return jsonify({"message": "Task deleted!"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
    import os