// Theme toggle functionality
(function() {
    // Get the current theme from localStorage or default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the theme immediately to avoid flash
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
    
    // Function to toggle theme
    function toggleTheme() {
        const html = document.documentElement;
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        // Update the theme
        html.setAttribute('data-theme', newTheme);
        
        // Save to localStorage
        localStorage.setItem('theme', newTheme);
        
        // Update button text
        updateButtonText(newTheme);
    }
    
    // Function to update button text
    function updateButtonText(theme) {
        const button = document.getElementById('themeToggle');
        if (button) {
            button.textContent = theme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
        }
    }
    
    // Initialize when DOM is loaded
    document.addEventListener('DOMContentLoaded', function() {
        // Create and add the toggle button to footer
        const footer = document.querySelector('footer');
        if (footer) {
            const button = document.createElement('button');
            button.id = 'themeToggle';
            button.className = 'theme-toggle';
            button.setAttribute('aria-label', 'Toggle theme');
            
            // Set initial button text
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
            button.textContent = currentTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
            
            // Add click event
            button.addEventListener('click', toggleTheme);
            
            // Add to footer
            footer.appendChild(button);
        }
    });
})();
