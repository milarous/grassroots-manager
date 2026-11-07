let selectedSlot = null;

// Opens the save modal and shows the initial slot selection
function openSaveModal() {
    const modal = document.getElementById('saveModal');
    const slotsContainer = document.getElementById('saveSlotsContainer');
    const saveForm = document.getElementById('saveForm');

    // Ensure we have the global saveSlots variable
    if (typeof saveSlots === 'undefined') {
        console.error("saveSlots is not defined. Make sure it's included in the page.");
        return;
    }

    // Clear previous slot buttons
    slotsContainer.innerHTML = '';

    // Create buttons for each slot
    for (let i = 1; i <= 3; i++) {
        const slot = i.toString();
        const slotData = saveSlots[slot];
        const button = document.createElement('button');
        button.className = 'slot-btn';
        button.onclick = () => showSaveForm(i);
        
        let buttonText = `Slot ${i}`;
        if (slotData && slotData.exists) {
            buttonText += ` - ${slotData.label}`;
        } else {
            buttonText += ' (Empty)';
        }
        button.textContent = buttonText;
        slotsContainer.appendChild(button);
    }

    // Show slot selection and hide the form
    slotsContainer.classList.remove('hidden');
    saveForm.classList.add('hidden');
    
    // Show the modal
    modal.classList.add('show');
}

// Hides the slot selection and shows the save form for a specific slot
function showSaveForm(slot) {
    selectedSlot = slot;
    const slotsContainer = document.getElementById('saveSlotsContainer');
    const saveForm = document.getElementById('saveForm');
    const saveLabelInput = document.getElementById('saveLabel');
    const saveGameForm = document.getElementById('saveGameForm');

    const slotData = saveSlots[selectedSlot.toString()];

    // Set the form's action
    saveGameForm.action = `/save_game/${selectedSlot}`;

    // Pre-fill the label if it exists
    if (slotData && slotData.exists) {
        saveLabelInput.value = slotData.label;
    } else {
        saveLabelInput.value = '';
    }

    // Swap visibility
    slotsContainer.classList.add('hidden');
    saveForm.classList.remove('hidden');
    saveLabelInput.focus();
}

// Hides the save form and shows the slot selection
function showSaveSlots() {
    const slotsContainer = document.getElementById('saveSlotsContainer');
    const saveForm = document.getElementById('saveForm');

    slotsContainer.classList.remove('hidden');
    saveForm.classList.add('hidden');
}

// Closes the save modal
function closeSaveModal() {
    const modal = document.getElementById('saveModal');
    modal.classList.remove('show');
    selectedSlot = null;
}
