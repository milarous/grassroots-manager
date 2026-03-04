const viewAttendanceModal = document.getElementById('viewAttendanceModal');
const attendanceReportList = document.getElementById('attendance-list');
const attendanceReportTitle = document.getElementById('view-attendance-title');

function openViewAttendanceModal(attendees, eventName, eventWeek, eventYear) {
    attendanceReportList.innerHTML = ''; // Clear previous content

    // Set modal title
    attendanceReportTitle.textContent = `${eventName} (Week ${eventWeek}, ${eventYear})`;

    if (Array.isArray(attendees) && attendees.length > 0) {
        attendees.forEach(player => {
            const playerItem = document.createElement('li');
            playerItem.classList.add('contact-item');

            const sourceBadge = player.source ? `<span class="player-source">${player.source}</span>` : '';

            playerItem.innerHTML = `
                <div class="contact-info">
                    <strong>${player.name}</strong>
                    <div style="display: flex; align-items: center; margin-top: 4px;">
                        <span class="contact-details">Age: ${player.age}</span>
                        ${sourceBadge}
                    </div>
                </div>
            `;
            attendanceReportList.appendChild(playerItem);
        });
    } else {
        const noPlayersItem = document.createElement('li');
        noPlayersItem.textContent = 'No attendees to display.';
        attendanceReportList.appendChild(noPlayersItem);
    }

    viewAttendanceModal.classList.add('show');
}

function closeViewAttendanceModal() {
    viewAttendanceModal.classList.remove('show');
}
