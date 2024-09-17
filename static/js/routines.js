const DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

fetch('/api/routines')
    .then(response => response.json())
    .then(data => {
        const routineList = document.getElementById('routine-list');
        data.forEach(routine => {
            const taskCard = document.createElement('div');
            const taskDay = document.createElement('span');
            const taskDeleteButton = document.createElement('button');
            const taskTitle = document.createElement('h3');
            const taskNotes = document.createElement('span');

            taskDay.textContent = DAYS[routine.taskDayOfWeek];
            taskTitle.textContent = routine.taskName;
            taskNotes.textContent = routine.taskNotes;

            taskDeleteButton.textContent = '×'; // Use '×' for the X symbol
            taskDeleteButton.classList.add('task-delete-button');

            taskDeleteButton.addEventListener('click', () => {
                taskCard.remove();

                fetch(`api/routines/delete/${routine._id}`, {
                    method: 'DELETE'
                }).then(response => {
                    if (response.ok) {
                        console.log('deu bom');
                    } else {
                        console.log('deu ruim');
                    }
                }); 
            });

            taskCard.appendChild(taskDay);
            taskCard.appendChild(taskDeleteButton);
            taskCard.appendChild(taskTitle);
            taskCard.appendChild(taskNotes);
            
            taskCard.classList.add('col-6')

            routineList.appendChild(taskCard);
        });
    });