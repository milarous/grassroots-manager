const viewInvitedModal = document.getElementById('viewInvitedModal');
const invitedList = document.getElementById('invited-list');
const invitedModalTitle = document.getElementById('view-invited-title');

function openViewInvitedModal(invitedContacts, eventName, eventWeek, eventYear) {
    invitedList.innerHTML = ''; // Clear previous list

    // Set modal title
    invitedModalTitle.textContent = `${eventName} (Week ${eventWeek}, ${eventYear})`;

    if (Array.isArray(invitedContacts) && invitedContacts.length > 0) {
        invitedContacts.forEach(player => {
            const listItem = document.createElement('li');
            listItem.className = 'contact-item';

            const sourceBadge = player.source ? `<span class="player-source">${player.source}</span>` : '';

            listItem.innerHTML = `
                <div class="contact-info">
                    <strong>${player.name}</strong>
                    <div style="display: flex; align-items: center; margin-top: 4px;">
                        <span class="contact-details">Age: ${player.age}</span>
                        ${sourceBadge}
                    </div>
                </div>
            `;
            invitedList.appendChild(listItem);
        });
    } else {
        const noPlayersMessage = document.createElement('li');
        noPlayersMessage.textContent = 'No players have been invited to this event yet.';
        invitedList.appendChild(noPlayersMessage);
    }

    viewInvitedModal.classList.add('show');
}

function closeViewInvitedModal() {
    viewInvitedModal.classList.remove('show');
}
