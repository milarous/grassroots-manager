// Call Modal JavaScript

let currentContact = null;

function openCallModal(playerName, playerIndex, clubName) {
    currentContact = {
        name: playerName,
        index: playerIndex
    };
    
    const modal = document.getElementById('callModal');
    const contactSpeech = document.getElementById('contactSpeech');
    const initialButtons = document.getElementById('initialButtons');
    const responseOptions = document.getElementById('responseOptions');
    const trainingSelection = document.getElementById('trainingSelection');
    const clubNameInButton = document.getElementById('clubNameInButton');
    
    // Display the greeting
    contactSpeech.textContent = `Hello, ${playerName} speaking.`;
    
    // Set club name in button
    clubNameInButton.textContent = clubName;
    
    // Show initial buttons, hide others
    initialButtons.style.display = 'flex';
    responseOptions.style.display = 'none';
    trainingSelection.style.display = 'none';
    
    modal.classList.add('show');
    
    // After a short delay, show response options
    setTimeout(() => {
        initialButtons.style.display = 'none';
        responseOptions.style.display = 'flex';
    }, 1500);
}

function wrongNumber() {
    const contactSpeech = document.getElementById('contactSpeech');
    contactSpeech.textContent = `Oh, no worries. Have a good day!`;
    
    // Close after a brief moment
    setTimeout(() => {
        hangUp();
    }, 1500);
}

function inviteToTraining() {
    if (!currentContact) return;
    
    const contactSpeech = document.getElementById('contactSpeech');
    const responseOptions = document.getElementById('responseOptions');
    const trainingSelection = document.getElementById('trainingSelection');
    
    contactSpeech.textContent = `That sounds interesting! When are the training sessions?`;
    responseOptions.style.display = 'none';
    
    // Fetch available training sessions
    fetch(`/invite_to_training/${currentContact.index}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const sessionsList = document.getElementById('trainingSessionsList');
            
            if (data.training_sessions.length > 0) {
                // Show training sessions
                sessionsList.innerHTML = '<p style="margin-bottom: 10px; text-align: center;">Select a training session:</p>';
                data.training_sessions.forEach(session => {
                    const button = document.createElement('button');
                    button.className = 'menu-button';
                    button.textContent = `${session.name} - Week ${session.week}, ${session.year}`;
                    button.onclick = () => selectTrainingSession(session.index);
                    sessionsList.appendChild(button);
                });
            } else {
                // No sessions available
                sessionsList.innerHTML = '<p style="text-align: center;">We don\'t have any sessions scheduled yet, but we\'ll get back to you soon!</p>';
                contactSpeech.textContent = `Okay, sounds good. Looking forward to hearing from you!`;
                
                setTimeout(() => {
                    hangUp();
                }, 2500);
            }
            
            trainingSelection.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        hangUp();
    });
}

function selectTrainingSession(trainingIndex) {
    if (!currentContact) return;
    
    const contactSpeech = document.getElementById('contactSpeech');
    contactSpeech.textContent = `Perfect! I'll be there. See you then!`;
    
    // Add contact to the selected training session
    fetch(`/add_contact_to_training/${currentContact.index}/${trainingIndex}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            setTimeout(() => {
                hangUp();
                // Reload to show updated UI
                window.location.reload();
            }, 1500);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        hangUp();
    });
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
