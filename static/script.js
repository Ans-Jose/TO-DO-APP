// ---------------- To-Do List ----------------
const taskInput = document.getElementById("taskInput");
const dateInput = document.getElementById("dateInput");
const timeInput = document.getElementById("timeInput");
const taskList = document.getElementById("taskList");

async function loadTasks() {
    const res = await fetch('/tasks');
    const data = await res.json();

    taskList.innerHTML = '';
    data.forEach(taskObj => {
        const li = document.createElement('li');
        li.innerHTML = `
            <div class="task-content">
                <span class="task-name">${taskObj.task}</span>
                <span class="task-date">${taskObj.date}</span>
                <span class="task-time">${taskObj.time}</span>
            </div>
            <button>Delete</button>
        `;
        li.querySelector('button').onclick = () => deleteTask(taskObj.id);
        taskList.appendChild(li);
    });
}

async function addTask() {
    const task = taskInput.value.trim();
    const date = dateInput.value;
    const time = timeInput.value;
    if (!task || !date || !time) return;

    await fetch('/tasks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({task, date, time})
    });

    taskInput.value = '';
    dateInput.value = '';
    timeInput.value = '';
    loadTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    loadTasks();
}
