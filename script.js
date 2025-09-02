const taskInput = document.getElementById("taskInput");
const dateInput = document.getElementById("dateInput");
const timeInput = document.getElementById("timeInput");
const taskList = document.getElementById("taskList");

let tasks = []; // store tasks in memory

function addTask() {
    const task = taskInput.value;
    const date = dateInput.value;
    const time = timeInput.value;

    if (!task) return;

    const taskData = { task, date, time };
    tasks.push(taskData);
    renderTasks();

    taskInput.value = "";
    dateInput.value = "";
    timeInput.value = "";
}

function deleteTask(index) {
    tasks.splice(index, 1);
    renderTasks();
}

function renderTasks() {
    taskList.innerHTML = "";
    tasks.forEach((t, i) => {
        const li = document.createElement("li");

        li.innerHTML = `
            <div class="task-content">
                <span class="task-name">${t.task}</span>
                <span class="task-date">${t.date}</span>
                <span class="task-time">${t.time}</span>
            </div>
            <button onclick="deleteTask(${i})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

