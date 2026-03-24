// Call Modal JavaScript

let currentContact = null;
let isWrongNumber = false;

function openCallModal(playerName, playerIndex, clubName, playerSource) {
    currentContact = {
        name: playerName,
        index: playerIndex,
        isFromTraining: playerSource && playerSource.includes('Open Training')
    };
    
    const modal = document.getElementById('callModal');
    const contactSpeech = document.getElementById('contactSpeech');
    const responseOptions = document.getElementById('responseOptions');
    const farewellOptions = document.getElementById('farewellOptions');
    const trainingSelection = document.getElementById('trainingSelection');
    const clubNameInButton = document.getElementById('clubNameInButton');
    
    // Update message based on source
    if (currentContact.isFromTraining) {
        contactSpeech.textContent = `Hi, I'm calling from ${clubName}. Thanks so much for coming to our Open Training Session. I don't think we're the right club for you...`;
        
        // Add specific options for training followup
        responseOptions.innerHTML = `
            <button class="menu-button inline" onclick="recruitFromTraining()">Hi, I loved what I saw out there at the Open Training session, would you like to join our squad?</button>
            <button class="menu-button inline" onclick="sayGoodbye()">No worries, thanks for your time.</button>
        `;
        
        isWrongNumber = false; // Disable wrong number for training follow-up
    } else {
        // 5% chance of wrong number for regular contacts
        isWrongNumber = Math.random() < 0.05;
        
        if (isWrongNumber) {
            contactSpeech.textContent = `The number you have dialed has been disconnected.`;
        } else {
            contactSpeech.textContent = `Hello, ${playerName} speaking.`;
            clubNameInButton.textContent = clubName;
        }

        // Add original options for normal contacts
        responseOptions.innerHTML = `
            <button class="menu-button inline" onclick="inviteToTraining()">Invite to Training</button>
            <button class="menu-button inline" onclick="sayGoodbye()">Hang up</button>
        `;
    }
    
    // Hide all option sections initially
    responseOptions.style.display = 'none';
    farewellOptions.style.display = 'none';
    trainingSelection.style.display = 'none';
    
    modal.classList.add('show');
    
    // After a short delay, show response options
    if (!isWrongNumber) {
        setTimeout(() => {
            responseOptions.style.display = 'flex';
        }, 1500);
    }
}

function confirmIgnore(index) {
    if (confirm('Are you sure you want to ignore this player?')) {
        document.getElementById('ignoreForm-' + index).submit();
    }
}

function recruitFromTraining() {
    // Navigate to recruit
    if (!currentContact) return;
    document.getElementById('ignoreForm-' + currentContact.index).action = '/recruit_follow_up/' + currentContact.index;
    document.getElementById('ignoreForm-' + currentContact.index).querySelector('input[name="action"]').value = 'recruit';
    document.getElementById('ignoreForm-' + currentContact.index).submit();
}

function wrongNumber() {
    const contactSpeech = document.getElementById('contactSpeech');
    contactSpeech.textContent = `Oh, no worries. Have a good day!`;
    
    // Close after a brief moment
    setTimeout(() => {
        hangUp();
    }, 1500);
}

function sayGoodbye() {
    const contactSpeech = document.getElementById('contactSpeech');
    const farewellOptions = document.getElementById('farewellOptions');
    
    contactSpeech.textContent = `You too, bye!`;
    farewellOptions.style.display = 'none';
    
    // Mark for removal and close after a brief moment
    if (currentContact) {
        // If from training, don't necessarily remove (though maybe we should?)
        // The task implies recruitment or not. Let's just hang up for now.
        if (currentContact.isFromTraining) {
             setTimeout(() => {
                hangUp();
            }, 1000);
            return;
        }
        
        fetch(`/remove_contact/${currentContact.index}?reason=not_interested`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            setTimeout(() => {
                hangUp();
                if (data.success) {
                    // Reload to show updated contact list
                    window.location.reload();
                }
            }, 1500);
        })
        .catch(error => {
            console.error('Error:', error);
            setTimeout(() => {
                hangUp();
            }, 1500);
        });
    }
}

function inviteToTraining() {
    if (!currentContact) return;
    
    const contactSpeech = document.getElementById('contactSpeech');
    const responseOptions = document.getElementById('responseOptions');
    const farewellOptions = document.getElementById('farewellOptions');
    const trainingSelection = document.getElementById('trainingSelection');
    
    // Hide response options
    responseOptions.style.display = 'none';
    
    // 10% chance they say no
    const isNotInterested = Math.random() < 0.10;
    
    if (isNotInterested) {
        // Contact is not interested
        contactSpeech.textContent = `No thanks, I'm not interested.`;
        farewellOptions.style.display = 'flex';
    } else {
        // Contact is interested
        contactSpeech.textContent = `Yes, that sounds interesting! When are the training sessions?`;
        
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
    
    // If wrong number, remove contact from list
    if (isWrongNumber && currentContact) {
        fetch(`/remove_contact/${currentContact.index}?reason=disconnected`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Reload to show updated contact list
                window.location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    currentContact = null;
    isWrongNumber = false;
}

// Close modal when clicking outside of it
window.addEventListener('click', function(event) {
    const modal = document.getElementById('callModal');
    if (event.target === modal) {
        hangUp();
    }
});
