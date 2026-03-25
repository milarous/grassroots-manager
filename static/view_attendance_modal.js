function handleViewAttendance(buttonElement) {
    try {
        const attendees = JSON.parse(buttonElement.dataset.attendees.replace(/'/g, '"'));
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
    modal.querySelector('#view-attendance-title').textContent = `${eventName} Attendance`;
    
    // Distinguish between invited and walk-in
    // We assume invited if source indicates it, but since we rely on attendee dicts, let's just group them by source
    // Since attendees are just a list of dicts, let's categorize them for display
    
    const contentEl = modal.querySelector('#attendance-list');
    contentEl.innerHTML = `
        <h3>Week ${eventWeek}, ${eventYear}</h3>
        <p>${attendees.length} player(s) attended</p>
        ${attendees.map(player => `
            <li class="contact-item">
                <div class="contact-info">
                    <strong>${player.name}</strong> 
                    <span class="badge ${player.source.includes('Invited') ? 'invited-badge' : 'walkin-badge'}">${player.source.includes('Invited') ? 'Invited' : 'Walk-in'}</span>
                    <span class="contact-details">Age: ${player.age} | Pos: ${player.position} | Skill: ${player.skill_level}</span>
                    <span class="player-source">${player.source}</span>
                </div>
            </li>`).join('')}
    `;

    modal.style.display = 'block';
}
