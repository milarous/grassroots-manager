// Call Modal JavaScript

let currentContact = null;

function openCallModal(playerName, playerIndex) {
    currentContact = {
        name: playerName,
        index: playerIndex
    };
    
    const modal = document.getElementById('callModal');
    const contactSpeech = document.getElementById('contactSpeech');
    
    // Display the greeting
    contactSpeech.textContent = `Hello, ${playerName} speaking.`;
    
    modal.classList.add('show');
}

function hangUp() {
    const modal = document.getElementById('callModal');
    modal.classList.remove('show');
    currentContact = null;
}

// Close modal when clicking outside of it
window.addEventListener('click', function(event) {
    const modal = document.getElementById('callModal');
    if (event.target === modal) {
        hangUp();
    }
});
