// Load tasks when the page opens
async function loadTasks() {
  const res = await fetch('/tasks');
  const data = await res.json();
  
  const taskList = document.getElementById('taskList');
  taskList.innerHTML = '';
  
  data.forEach((taskObj, index) => {
    const li = document.createElement('li');

    // Task content container
    const taskContent = document.createElement('div');
    taskContent.className = 'task-content';
    taskContent.innerHTML = `
      <span class="task-name">${taskObj.task}</span>
      <span class="task-date">${taskObj.date}</span>
      <span class="task-time">${taskObj.time}</span>
    `;

    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.onclick = () => deleteTask(index);

    li.appendChild(taskContent);
    li.appendChild(delBtn);
    taskList.appendChild(li);
  });
}

// Add new task
async function addTask() {
    const taskInput = document.getElementById('taskInput');
    const dateInput = document.getElementById('dateInput');
    const timeInput = document.getElementById('timeInput');

    const task = taskInput.value.trim();
    const date = dateInput.value;
    const time = timeInput.value;

    if (!task || !date || !time) return; // require all fields

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

// Delete a task
async function deleteTask(id) {
  await fetch(`/tasks/${id}`, {method: 'DELETE'});
  loadTasks();
}

// Run when page loads
window.onload = loadTasks;
