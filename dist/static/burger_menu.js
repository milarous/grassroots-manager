// Burger Menu functionality

function initializeBurgerMenu() {
    const burgerBtn = document.getElementById('burgerBtn');
    const burgerDropdown = document.getElementById('burgerDropdown');
    
    if (!burgerBtn || !burgerDropdown) return;
    
    // Toggle menu on button click
    burgerBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        burgerDropdown.classList.toggle('show');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.burger-menu')) {
            burgerDropdown.classList.remove('show');
        }
    });
    
    // Close menu when clicking on a menu item
    burgerDropdown.addEventListener('click', () => {
        burgerDropdown.classList.remove('show');
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initializeBurgerMenu);
