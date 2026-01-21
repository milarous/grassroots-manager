// Load Modal functionality

let deleteSlotConfirm = null;

function openLoadModal() {
    document.getElementById('loadModal').classList.add('show');
}

function closeLoadModal() {
    document.getElementById('loadModal').classList.remove('show');
}

function loadGame(slot) {
    window.location.href = '/load_game/' + slot;
}

function deleteGame(slot) {
    if (confirm('Are you sure you want to delete this save? This cannot be undone.')) {
        window.location.href = '/delete_game/' + slot;
    }
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    var loadModal = document.getElementById('loadModal');
    if (event.target == loadModal) {
        closeLoadModal();
    }
}
