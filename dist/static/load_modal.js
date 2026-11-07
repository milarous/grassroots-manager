// Load Modal functionality - can be included in any template

function openLoadModal() {
    initializeLoadModal();
    backToSlotSelectionLoad();
    document.getElementById('loadModal').classList.add('show');
}

function closeLoadModal() {
    document.getElementById('loadModal').classList.remove('show');
}

function initializeLoadModal() {
    const container = document.getElementById('slotButtonsContainerLoad');
    if (!container || !saveSlots) return;
    
    container.innerHTML = '';
    
    for (let slot = 1; slot <= 3; slot++) {
        const slotData = saveSlots[slot.toString()];
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'slot-btn';
        button.onclick = () => selectSlotLoad(slot);
        
        let buttonText = `Slot ${slot}`;
        if (slotData.exists) {
            buttonText += ` - ${slotData.label}`;
        } else {
            buttonText += ' (Empty)';
            button.disabled = true;
        }
        
        button.innerHTML = buttonText;
        container.appendChild(button);
    }
}

function selectSlotLoad(slot) {
    const slotData = saveSlots[slot.toString()];
    
    // Update UI to show confirm step
    document.getElementById('slotSelectionStepLoad').classList.add('hidden');
    document.getElementById('loadConfirmStep').classList.remove('hidden');
    document.getElementById('backBtnLoad').classList.remove('hidden');
    document.getElementById('confirmBtnLoad').classList.remove('hidden');
    
    // Show selected slot details
    let infoHtml = `<strong>Loading from Slot ${slot}</strong><br><br>`;
    infoHtml += `<strong>Save Details:</strong><br>`;
    infoHtml += `Label: ${slotData.label}<br>`;
    infoHtml += `Game Progress: ${slotData.game_date}<br>`;
    infoHtml += `Save Time: ${slotData.timestamp}<br>`;
    if (slotData.club_info) {
        infoHtml += `<br>Club: ${slotData.club_info.name}<br>`;
        infoHtml += `Location: ${slotData.club_info.city}, ${slotData.club_info.country}<br>`;
        infoHtml += `Finances: $${slotData.club_info.finances}<br>`;
        infoHtml += `Reputation: ${slotData.club_info.reputation}`;
    }
    
    document.getElementById('selectedSlotInfoLoad').innerHTML = infoHtml;
    window.selectedLoadSlot = slot;
}

function backToSlotSelectionLoad() {
    document.getElementById('slotSelectionStepLoad').classList.remove('hidden');
    document.getElementById('loadConfirmStep').classList.add('hidden');
    document.getElementById('backBtnLoad').classList.add('hidden');
    document.getElementById('confirmBtnLoad').classList.add('hidden');
    window.selectedLoadSlot = null;
}

function confirmLoad() {
    if (window.selectedLoadSlot === null) {
        alert('Please select a slot first');
        return;
    }
    window.location.href = '/load_game/' + window.selectedLoadSlot;
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('loadModal');
    if (modal && event.target === modal) {
        closeLoadModal();
    }
}
