// -----------------------------
// Universal Modal Closer
// -----------------------------

window.onclick = function(event) {
    // Get all modals that are currently displayed
    const modals = document.querySelectorAll('.modal, .save-modal');

    modals.forEach(modal => {
        if (event.target == modal) {
            // Check which modal is being clicked on and close it
            if (modal.id === 'saveModal') {
                closeSaveModal();
            } else if (modal.id === 'viewInvitedModal') {
                closeViewInvitedModal();
            } else if (modal.id === 'viewAttendanceModal') {
                closeViewAttendanceModal();
            } else if (modal.id === 'loadModal') {
                closeLoadModal();
            }
        }
    });
}

// -----------------------------
// View Invitees Modal
// -----------------------------

function handleViewInvited(buttonElement) {
    try {
        const invitedContacts = JSON.parse(buttonElement.dataset.invited.replace(/'/g, '"'));
        const eventName = buttonElement.dataset.name;
        const eventWeek = parseInt(buttonElement.dataset.week);
        const eventYear = parseInt(buttonElement.dataset.year);
        
        openViewInvitedModal(invitedContacts, eventName, eventWeek, eventYear);
    } catch (error) {
        console.error('Error handling view invited modal:', error);
        alert('Failed to load training event details: ' + error.message);
    }
}

function openViewInvitedModal(invitedContacts, eventName, eventWeek, eventYear) {
    const modal = document.getElementById('viewInvitedModal');
    modal.querySelector('#view-invited-title').textContent = `${eventName} Invitees`;
    
    const contentEl = modal.querySelector('#invited-list');
    contentEl.innerHTML = `
        <h3>Week ${eventWeek}, ${eventYear}</h3>
        <p>${invitedContacts.length} invited player(s)</p>
        ${invitedContacts.map(player => `
            <li class="contact-item">
                <div class="contact-info">
                    <strong>${player.name}</strong>
                    <span class="contact-details">Age: ${player.age} | Pos: ${player.position} | Skill: ${player.skill_level}</span>
                    <span class="player-source">${player.source || 'Unknown'}</span>
                </div>
            </li>`).join('')}
    `;

    modal.classList.add("show");
}

function closeViewInvitedModal() {
    const modal = document.getElementById("viewInvitedModal");
    modal.classList.remove("show");
}

// -----------------------------
// View Attendance Modal
// -----------------------------

function handleViewAttendance(buttonElement) {
    try {
        const attendees = JSON.parse(buttonElement.dataset.attendees.replace(/'/g, '"'));
        const eventName = buttonElement.dataset.name;
        const eventWeek = parseInt(buttonElement.dataset.week);
        const eventYear = parseInt(buttonElement.dataset.year);
        
        openViewAttendanceModal(attendees, eventName, eventWeek, eventYear);
    } catch (error) {
        console.error('Error handling view attendance modal:', error);
        alert('Failed to load attendance details: ' + error.message);
    }
}

function openViewAttendanceModal(attendees, eventName, eventWeek, eventYear) {
    const modal = document.getElementById("viewAttendanceModal");
    modal.querySelector('#view-attendance-title').textContent = `${eventName} Attendance`;
    
    const contentEl = modal.querySelector('#attendance-list');
    
    // Sort players so invited are at the top, then walk-ins
    const sortedAttendees = attendees.slice().sort((a, b) => {
        const aInvited = a.source && a.source.includes('Invited');
        const bInvited = b.source && b.source.includes('Invited');
        return bInvited - aInvited;
    });

    contentEl.innerHTML = `
        <h3>Week ${eventWeek}, ${eventYear}</h3>
        <p>${attendees.length} player(s) attended</p>
        ${sortedAttendees.map(player => `
            <li class="contact-item">
                <div class="contact-info">
                    <strong>${player.name}</strong> 
                    <span class="badge ${player.source && player.source.includes('Invited') ? 'invited-badge' : 'walkin-badge'}">${player.source && player.source.includes('Invited') ? 'Invited' : 'Walk-in'}</span>
                    <span class="contact-details">Age: ${player.age} | Pos: ${player.position} | Skill: ${player.skill_level}</span>
                    <span class="player-source">${player.source}</span>
                </div>
            </li>`).join('')}
    `;

    modal.classList.add("show");
}

function closeViewAttendanceModal() {
    const modal = document.getElementById("viewAttendanceModal");
    modal.classList.remove("show");
}
