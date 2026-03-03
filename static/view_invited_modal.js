function openViewInvitedModal(invitedContacts) {
    const modal = document.getElementById('viewInvitedModal');
    const list = document.getElementById('invitedPlayersList');

    // Clear previous list
    list.innerHTML = '';

    // Populate the list with invited players
    if (invitedContacts && invitedContacts.length > 0) {
        invitedContacts.forEach(player => {
            const listItem = document.createElement('div');
            listItem.className = 'week-result-item';

            // Create a badge for the source using the correct class
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
            list.appendChild(listItem);
        });
    } else {
        const noPlayersMessage = document.createElement('p');
        noPlayersMessage.textContent = 'No players have been invited to this event yet.';
        list.appendChild(noPlayersMessage);
    }

    modal.style.display = 'block';
}

function closeViewInvitedModal() {
    const modal = document.getElementById('viewInvitedModal');
    modal.style.display = 'none';
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    const modal = document.getElementById('viewInvitedModal');
    if (event.target == modal) {
        closeViewInvitedModal();
    }
}
