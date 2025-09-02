
async function fetchPast() {
    const response = await fetch('/past_records');
    const records = await response.json();
    const pastList = document.getElementById('pastList');
    pastList.innerHTML = '';

    records.forEach(rec => {
        const li = document.createElement('li');
        li.className = 'past-row'; // unified class for CSS

        // Task column
        const taskSpan = document.createElement('span');
        taskSpan.className = 'past-task';
        taskSpan.textContent = rec.task;

        // Success column
        const successSpan = document.createElement('span');
        successSpan.className = 'past-success';
        successSpan.textContent = rec.status.toLowerCase() === 'success' ? '✅' : '';

        // Failure column
        const failureSpan = document.createElement('span');
        failureSpan.className = 'past-failure';
        failureSpan.textContent = rec.status.toLowerCase() === 'failure' ? '❌' : '';

        // Delete button column
        const btn = document.createElement('button');
        btn.textContent = 'Delete';
        btn.onclick = () => deletePast(rec.id);

        // Append columns
        li.appendChild(taskSpan);
        li.appendChild(successSpan);
        li.appendChild(failureSpan);
        li.appendChild(btn);

        pastList.appendChild(li);
    });
}
