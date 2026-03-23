function handleViewInvited(buttonElement) {
    try {
        const invitedContacts = JSON.parse(buttonElement.dataset.invited);
        const eventName = buttonElement.dataset.name;
        const eventWeek = parseInt(buttonElement.dataset.week);
        const eventYear = parseInt(buttonElement.dataset.year);
        
        openViewInvitedModal(invitedContacts, eventName, eventWeek, eventYear);
    } catch (error) {
        console.error('Error handling view invited modal:', error);
        alert('Failed to load training event details. Please try again.');
    }
}

function openViewInvitedModal(invitedContacts, eventName, eventWeek, eventYear) {
    // Existing modal opening logic here
    const modal = document.getElementById('viewInvitedModal');
    modal.querySelector('.modal-title').textContent = `${eventName} Invitees`;
    
    const contentEl = modal.querySelector('.modal-content-body');
    contentEl.innerHTML = `
        <h3>Week ${eventWeek}, ${eventYear}</h3>
        <p>${invitedContacts.length} invited player(s)</p>
        <ul class="contacts-list">
            ${invitedContacts.map(player => `
                <li class="contact-item">
                    <div class="contact-info">
                        <strong>${player.name}</strong>
                        <span>Age: ${player.age}</span>
                    </div>
                </li>`).join('')}
        </ul>
    `;

    modal.style.display = 'block';
}