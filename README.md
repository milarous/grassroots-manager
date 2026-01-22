# Grassroots Football Manager

A simple web-based football management simulation game built with Flask. Manage your grassroots football club from the ground up, starting with basic finances and reputation, and build your squad and facilities.

## Features

- Create and customize your football club
- View club overview including finances, reputation, and facilities
- Scout and recruit senior players to build your squad
- **Search for and rent facilities** - Start without a facility and choose from 4 available facilities in Adelaide to rent monthly:
  - Hackham Soccer Complex ($800/month)
  - Findon Sports Park ($1,200/month)
  - Salisbury Sports Ground ($950/month)
  - Campbelltown Football Ground ($1,100/month)
- Switch between facilities at any time
- View competitions (basic view)
- Save and load game progress (3 save slots) - Facility data is automatically saved
- Simple web interface with HTML templates

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

Run the application:
```
python main.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to start the game.

**Gameplay Guide:**
- **Start by creating your club** on the main menu (select your country and city).
- **Club Overview**: View your club's current status including name, location, finances, reputation, and current facility.
- **Facilities**: 
  - If you don't have a facility yet, browse and select one of the 4 available facilities in Adelaide to rent.
  - Once you have rented a facility, the page shows your current facility details (name, location, monthly cost).
  - Click "Search for New Facility" to view other facilities and potentially switch to a different one.
  - The current facility is highlighted with a green badge.
- **Squad View**: Scout and recruit players to build your team.
- **Competitions**: View available competitions.
- **Save Your Game**: Use the "Save Game" button to save your progress to one of 3 slots. Your facility data will be included in the save.
- **Load Your Game**: Return to the main menu and load a previous game from a save slot.

## Requirements

- Python 3.x
- Flask
- See `requirements.txt` for full list of dependencies.

## Project Structure

- `main.py`: Main Flask application and game logic
- `templates/`: HTML templates for the web interface
  - `index.html`: Main menu and club creation
  - `club.html`: Club overview
  - `squad.html`: Squad management
  - `facilities.html`: Facilities view
  - `competitions.html`: Competitions view
  - `exit.html`: Exit page
- `requirements.txt`: Python dependencies