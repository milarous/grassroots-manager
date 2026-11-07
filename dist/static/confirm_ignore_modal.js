// Confirm Ignore Modal JavaScript

function openConfirmIgnoreModal(index) {
    const modal = document.getElementById('confirmIgnoreModal');
    const confirmBtn = document.getElementById('confirmIgnoreBtn');
    
    // Set up the confirmation button to submit the correct form
    confirmBtn.onclick = function() {
        document.getElementById('ignoreForm-' + index).submit();
    };
    
    modal.classList.add('show');
}

function closeConfirmIgnoreModal() {
    const modal = document.getElementById('confirmIgnoreModal');
    modal.classList.remove('show');
}

// Close modal when clicking outside of it
window.addEventListener('click', function(event) {
    const modal = document.getElementById('confirmIgnoreModal');
    if (event.target === modal) {
        closeConfirmIgnoreModal();
    }
});
