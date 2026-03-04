
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

function openViewInviteesModal(inviteesJson, eventName, week, year) {
    const modal = document.getElementById("viewInvitedModal");
    const invitees = JSON.parse(inviteesJson);
    const list = document.getElementById("invited-list");
    list.innerHTML = "";

    document.getElementById("view-invited-title").textContent = `Invitees for ${eventName} (Week ${week}, ${year})`;

    if (invitees.length > 0) {
        invitees.forEach(invitee => {
            const li = document.createElement("li");
            li.textContent = invitee.name;
            list.appendChild(li);
        });
    } else {
        const li = document.createElement("li");
        li.textContent = "No players invited.";
        list.appendChild(li);
    }

    modal.classList.add("show");
}

function closeViewInvitedModal() {
    const modal = document.getElementById("viewInvitedModal");
    modal.classList.remove("show");
}

// -----------------------------
// View Attendance Modal
// -----------------------------

function openViewAttendanceModal(attendeesJson, eventName, week, year) {
    const modal = document.getElementById("viewAttendanceModal");
    const attendees = JSON.parse(attendeesJson);
    const list = document.getElementById("attendance-list");
    list.innerHTML = "";

    document.getElementById("view-attendance-title").textContent = `Attendance for ${eventName} (Week ${week}, ${year})`;

    if (attendees.length > 0) {
        attendees.forEach(attendee => {
            const li = document.createElement("li");
            li.textContent = attendee.name;
            list.appendChild(li);
        });
    } else {
        const li = document.createElement("li");
        li.textContent = "No players attended.";
        list.appendChild(li);
    }

    modal.classList.add("show");
}

function closeViewAttendanceModal() {
    const modal = document.getElementById("viewAttendanceModal");
    modal.classList.remove("show");
}
