# Grassroots Football Manager

A web-based football management simulation game built with Flask. Manage your grassroots football club from the ground up, starting with basic finances and reputation, and build your squad and facilities. Features a modern UI with modal dialogs, interactive save/load system, and responsive navigation.

## Features

### Core Gameplay
- **Club Creation**: Create and customize your football club with name, city, and country selection
- **Club Management**: View club overview including finances, reputation, and facilities
- **Squad Management**: Scout and recruit senior players to build your squad with detailed player information (name, age, position, skill level)
- **Facility Rental System**: Start without a facility and rent one from 4 available options in Adelaide:
  - Hackham Soccer Complex ($800/month)
  - Findon Sports Park ($1,200/month)
  - Salisbury Sports Ground ($950/month)
  - Campbelltown Football Ground ($1,100/month)
- **Switch Facilities**: Search for and switch to a different facility at any time
- **Competitions View**: Track available competitions (basic view)

### Save System
- **3 Save Slots**: Save your game progress in up to 3 different slots
- **Custom Labels**: Add custom labels to your saves for easy identification
- **Save Information**: View timestamps, club details, and facility information for each save
- **Load/Delete**: Load previous games or delete old saves
- **Modal Interface**: User-friendly modal dialogs for saving and loading
- **Facility Persistence**: Facility data is automatically saved and restored

### User Interface
- **Modern Web Interface**: Clean, responsive HTML/CSS design
- **Navigation Menu**: Easy-to-use left-side navigation menu on all game pages
- **Interactive Modals**: Modal dialogs for club creation, saving, and loading
- **Visual Feedback**: Button states, hover effects, and active page indicators
- **Footer Branding**: Consistent footer with copyright and version information

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/milarous/grassroots-manager.git
   cd grassroots-manager
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Starting the Game

Run the application:
```
python main.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to start the game.

### Playing the Game

1. **Main Menu**:
   - Click "Create Club" to start a new game
   - Click "Load Game" to continue from a saved slot
   - Click "Exit Game" to close

2. **Club Creation**:
   - Enter your club name
   - Select your country (currently: Australia)
   - Select your city (currently: Adelaide)
   - Click "Confirm" to create your club

3. **Game Navigation**:
   - Use the left sidebar menu to navigate between sections:
     - **Club Overview**: View finances, reputation, facility, and club details
     - **View Squad**: Manage your players
     - **View Facilities**: Rent and manage your club facilities
     - **View Competitions**: View available competitions
   - Click "Return to Main Menu" to go back to the main menu

4. **Squad Management**:
   - Click "Scout for Players" to generate 3 random available players
   - Click "Recruit" next to any available player to add them to your squad
   - View your current squad at the top of the page

5. **Facilities Management**:
   - If you don't have a facility yet, browse and select one of the 4 available facilities in Adelaide to rent
   - Once you have rented a facility, the page shows your current facility details (name, location, monthly cost)
   - Click "Search for New Facility" to view other facilities and potentially switch to a different one
   - The current facility is highlighted with a green badge and checkmark

6. **Saving Your Game**:
   - Click the "Save Game" button on any game page
   - Select one of the 3 available save slots
   - Enter a custom label for your save (e.g., "My First Club")
   - Click "Confirm" to save
   - Existing saves show their label, timestamp, club information, and facility details

7. **Loading a Game**:
   - From the main menu, click "Load Game"
   - Select a save slot to view its details
   - Click "Load" to continue from that save
   - Click "Back" to choose a different slot or "Cancel" to return to the main menu

## Requirements

- Python 3.x
- Flask
- See `requirements.txt` for full list of dependencies.

## Project Structure

```
grassroots-manager/
├── main.py                 # Main Flask application and game logic
│                           # - Club and Player classes
│                           # - Flask routes and game state management
│                           # - Save/load functionality with pickle
│
├── templates/              # HTML templates for the web interface
│   ├── index.html          # Main menu with club creation and load modals
│   ├── club.html           # Club overview page
│   ├── squad.html          # Squad management and player recruitment
│   ├── facilities.html     # Facilities view
│   ├── competitions.html   # Competitions view
│   ├── exit.html           # Exit page
│   └── _save_modal.html    # Reusable save modal component
│
├── static/                 # Static assets (CSS and JavaScript)
│   ├── styles.css          # Main stylesheet with:
│   │                       # - Base styles and layout
│   │                       # - Modal dialog styles
│   │                       # - Button and form styles
│   │                       # - Navigation menu styles
│   ├── save_modal.js       # Save modal functionality
│   └── load_modal.js       # Load modal functionality
│
├── saves/                  # Save game files (created automatically)
│   └── slot_*.pkl          # Pickled save data files
│
└── requirements.txt        # Python dependencies
```

### Key Components

- **Flask Application**: Built with Flask web framework for routing and template rendering
- **Game Logic**: Python classes for Club and Player management
- **Persistence**: Save system using Python's pickle module for serialization
- **Frontend**: HTML5, CSS3, and vanilla JavaScript for interactive UI
- **Modal System**: Reusable modal components for save/load operations