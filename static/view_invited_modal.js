console.log('view_invited_modal.js loaded');

function handleViewInvited(buttonElement) {
    console.log('handleViewInvited clicked', buttonElement);
    try {
        const data = buttonElement.dataset.invited;
        console.log('Raw data:', data);
        const invitedContacts = JSON.parse(data.replace(/'/g, '"'));
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
    // Existing modal opening logic here
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

    modal.style.display = 'block';
}