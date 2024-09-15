fetch('/api/routines')
    .then(response => response.json())
    .then(data => {
        const routineList = document.getElementById('routine-list');
        data.forEach(routine => {
            const listItem = document.createElement('li');
            listItem.textContent = `${routine.taskName} - ${routine.taskDayOfWeek} (${routine.taskNotes})`;
            routineList.appendChild(listItem);
        });
    });