function handleViewAttendance(buttonElement) {
    try {
        const attendees = JSON.parse(buttonElement.dataset.attendees);
        const eventName = buttonElement.dataset.name;
        const eventWeek = parseInt(buttonElement.dataset.week);
        const eventYear = parseInt(buttonElement.dataset.year);
        
        openViewAttendanceModal(attendees, eventName, eventWeek, eventYear);
    } catch (error) {
        console.error('Error handling view attendance modal:', error);
        alert('Failed to load attendance details. Please try again.');
    }
}

function openViewAttendanceModal(attendees, eventName, eventWeek, eventYear) {
    const modal = document.getElementById('viewAttendanceModal');
    modal.querySelector('.modal-title').textContent = `${eventName} Attendance`;
    
    const contentEl = modal.querySelector('.modal-content-body');
    contentEl.innerHTML = `
        <h3>Week ${eventWeek}, ${eventYear}</h3>
        <p>${attendees.length} player(s) attended</p>
        <ul class="contacts-list">
            ${attendees.map(player => `
                <li class="contact-item">
                    <div class="contact-info">
                        <strong>${player.name}</strong>
                        <span>Age: ${player.age}</span>
                        ${player.skill_level ? `<span>Skill: ${player.skill_level}</span>` : ''}
                    </div>
                </li>`).join('')}
        </ul>
    `;

    modal.style.display = 'block';
}