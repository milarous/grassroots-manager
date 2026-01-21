// Save Modal functionality - can be included in any template

let selectedSlot = null;

function initializeSaveModal() {
    const container = document.getElementById('slotButtonsContainer');
    if (!container || !saveSlots) return;
    
    container.innerHTML = '';
    
    for (let slot = 1; slot <= 3; slot++) {
        const slotData = saveSlots[slot.toString()];
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'slot-btn';
        button.onclick = () => selectSlot(slot);
        
        let buttonText = `Slot ${slot}`;
        if (slotData.exists) {
            buttonText += ` - ${slotData.label}`;
        } else {
            buttonText += ' (Empty)';
        }
        
        button.innerHTML = buttonText;
        container.appendChild(button);
    }
}

function selectSlot(slot) {
    selectedSlot = slot;
    const slotData = saveSlots[slot.toString()];
    
    // Update UI to show label/confirm step
    document.getElementById('slotSelectionStep').classList.add('hidden');
    document.getElementById('labelConfirmStep').classList.remove('hidden');
    document.getElementById('backBtn').classList.remove('hidden');
    document.getElementById('confirmBtn').classList.remove('hidden');
    
    // Show selected slot details
    let infoHtml = `<strong>${slotData.exists ? 'Overwriting' : 'Creating new save in'} Slot ${slot}</strong><br>`;
    
    if (slotData.exists) {
        infoHtml += `<br><strong>Current Save:</strong><br>`;
        infoHtml += `Label: ${slotData.label}<br>`;
        infoHtml += `Date: ${slotData.timestamp}<br>`;
        if (slotData.club_info) {
            infoHtml += `Club: ${slotData.club_info.name}<br>`;
            infoHtml += `Location: ${slotData.club_info.city}, ${slotData.club_info.country}<br>`;
            infoHtml += `Finances: $${slotData.club_info.finances}<br>`;
            infoHtml += `Reputation: ${slotData.club_info.reputation}`;
        }
    }
    
    document.getElementById('selectedSlotInfo').innerHTML = infoHtml;
    document.getElementById('saveLabel').value = slotData.exists ? slotData.label : '';
    document.getElementById('saveLabel').focus();
}

function backToSlotSelection() {
    selectedSlot = null;
    document.getElementById('slotSelectionStep').classList.remove('hidden');
    document.getElementById('labelConfirmStep').classList.add('hidden');
    document.getElementById('backBtn').classList.add('hidden');
    document.getElementById('confirmBtn').classList.add('hidden');
}

function openSaveModal() {
    initializeSaveModal();
    backToSlotSelection();
    document.getElementById('saveModal').classList.add('show');
}

function closeSaveModal() {
    document.getElementById('saveModal').classList.remove('show');
    selectedSlot = null;
}

function confirmSave() {
    if (selectedSlot === null) {
        alert('Please select a slot first');
        return;
    }
    
    const label = document.getElementById('saveLabel').value.trim();
    if (!label) {
        alert('Please enter a save label');
        return;
    }
    
    // Submit the save
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/save_game/' + selectedSlot;
    
    const labelInput = document.createElement('input');
    labelInput.type = 'hidden';
    labelInput.name = 'label';
    labelInput.value = label;
    
    form.appendChild(labelInput);
    document.body.appendChild(form);
    form.submit();
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('saveModal');
    if (modal && event.target === modal) {
        closeSaveModal();
    }
}
