const taskInput = document.getElementById("taskInput");
const dateInput = document.getElementById("dateInput");
const timeInput = document.getElementById("timeInput");
const taskList = document.getElementById("taskList");

// Load tasks when page loads
async function loadTasks() {
    const res = await fetch('/tasks');
    const data = await res.json();

    taskList.innerHTML = '';

    data.forEach((taskObj, index) => {
        const li = document.createElement('li');

        li.innerHTML = `
            <div class="task-content">
                <span class="task-name">${taskObj.task}</span>
                <span class="task-date">${taskObj.date}</span>
                <span class="task-time">${taskObj.time}</span>
            </div>
            <button>Delete</button>
        `;

        li.querySelector('button').onclick = () => deleteTask(index);
        taskList.appendChild(li);
    });}

// Add new


